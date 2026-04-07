import gradio as gr


def binary_search_steps(numbers, target):
    steps = []
    left = 0
    right = len(numbers) - 1
    step_number = 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = numbers[mid]

        steps.append(
            f"Step {step_number}: left = {left}, right = {right}, mid = {mid}, middle value = {mid_value}"
        )

        if mid_value == target:
            steps.append(f"Target {target} was found at index {mid}.")
            return f"Found at index {mid}", "\n".join(steps)

        elif mid_value < target:
            steps.append(
                f"{mid_value} is less than {target}, so search the right half."
            )
            left = mid + 1

        else:
            steps.append(
                f"{mid_value} is greater than {target}, so search the left half."
            )
            right = mid - 1

        step_number += 1

    steps.append(f"Target {target} was not found in the list.")
    return "Not found", "\n".join(steps)


def run_binary_search(user_input, target_input):
    try:
        numbers = [int(x.strip()) for x in user_input.split(",") if x.strip() != ""]
    except ValueError:
        return (
            "Invalid input",
            "Please enter only whole numbers separated by commas."
        )

    if not numbers:
        return (
            "Invalid input",
            "Please enter at least one number."
        )

    if numbers != sorted(numbers):
        return (
            "Invalid input",
            "Binary Search only works on a sorted list. Please enter numbers in increasing order."
        )

    try:
        target = int(target_input)
    except ValueError:
        return (
            "Invalid target",
            "Please enter a whole number as the target."
        )

    return binary_search_steps(numbers, target)


with gr.Blocks() as demo:
    gr.Markdown("# Binary Search Algorithm Simulation")
    gr.Markdown("Note: Binary Search works only on a sorted list in increasing order.")
    

    with gr.Row():
        user_input = gr.Textbox(
            label="Sorted List",
            placeholder="Example: 1, 3, 5, 7, 9, 11"
        )
        target_input = gr.Textbox(
            label="Target Value",
            placeholder="Example: 7"
        )

    run_button = gr.Button("Run Binary Search")

    result_output = gr.Textbox(label="Result")
    steps_output = gr.Textbox(label="Step by Step Explanation", lines=14)

    run_button.click(
        fn=run_binary_search,
        inputs=[user_input, target_input],
        outputs=[result_output, steps_output]
    )

demo.launch()