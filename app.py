import gradio as gr
from llm_testcase_generator import generate_test_cases
from testrail_integration import create_test_case

def process_input(story, project_id, suite_id, section_id):
    test_case_text = generate_test_cases(story)

    # You can improve parsing based on your format.
    steps = [{"content": "Step 1 placeholder", "expected": "Expected result"}]
    result = create_test_case(project_id, suite_id, section_id, "Generated Test Case", steps)

    return test_case_text + "\n\n✅ Test case pushed to TestRail!"

gr.Interface(
    fn=process_input,
    inputs=[
        gr.Textbox(label="User Story or Feature Description"),
        gr.Number(label="Project ID"),
        gr.Number(label="Suite ID"),
        gr.Number(label="Section ID"),
    ],
    outputs="text",
    title="TestRail Test Case Generator",
    description="Paste a requirement or user story and generate structured test cases to push into TestRail"
).launch(share=True)
