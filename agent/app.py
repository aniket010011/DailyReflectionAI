import pandas as pd

# Load tree
df = pd.read_csv("../tree/reflection-tree.tsv", sep="\t")

# Convert to dict
tree = df.set_index("id").to_dict(orient="index")

# State
state = {
    "answers": {},
    "signals": {
        "axis1": {"internal": 0, "external": 0},
        "axis2": {"contribution": 0, "entitlement": 0},
        "axis3": {"self": 0, "other": 0}
    }
}

# Get children
def get_children(parent_id):
    return df[df["parentId"] == parent_id]["id"].tolist()

# Apply signal
def apply_signal(signal):
    if pd.isna(signal) or signal == "":
        return
    axis, value = signal.split(":")
    state["signals"][axis][value] += 1

# Get dominant
def get_dominant(axis):
    values = state["signals"][axis]
    return max(values, key=values.get)

# Run tree
current_id = "START"

while True:
    node = tree[current_id]
    node_type = node["type"]
    text = str(node["text"]) if pd.notna(node["text"]) else ""

    # Replace placeholders
    for key, val in state["answers"].items():
        text = text.replace(f"{{{key}.answer}}", val)

    if node_type == "summary":
        text = text.replace("{axis1.dominant}", get_dominant("axis1"))
        text = text.replace("{axis2.dominant}", get_dominant("axis2"))
        text = text.replace("{axis3.dominant}", get_dominant("axis3"))

    print("\n" + text)

    # Apply signal
    apply_signal(node["signal"])

    # END
    if node_type == "end":
        break

    # QUESTION
    elif node_type == "question":
        options = node["options"].split("|")
        for i, opt in enumerate(options):
            print(f"{i+1}. {opt}")

        choice = int(input("Choose option: ")) - 1
        answer = options[choice]

        state["answers"][current_id] = answer

        # Move to next
        current_id = get_children(current_id)[0]

    # DECISION
    elif node_type == "decision":
        last_answer = list(state["answers"].values())[-1]
        rules = node["options"].split(";")

        for rule in rules:
            cond, target = rule.split(":")
            values = cond.replace("answer=", "").split("|")
            if last_answer in values:
                current_id = target
                break

    # AUTO-NODES (bridge / reflection / start)
    else:
        # If target exists 
        if pd.notna(node["target"]) and node["target"] != "":
            current_id = node["target"]
            continue   

        # Otherwise use children
        children = get_children(current_id)
        if children:
            current_id = children[0]
        else:
            break