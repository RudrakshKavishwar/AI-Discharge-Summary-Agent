# app.py

from langgraph.graph import StateGraph
import json
import os

from agents.planner import planner
from agents.extractor import extractor
from agents.reconciliation import reconcile
from agents.validator import validator
from agents.summary_generator import generate_summary

from tools.pdf_reader import pdf_to_images
from agents.gemini_ocr import extract_page_text


workflow = StateGraph(dict)

workflow.add_node("planner", planner)
workflow.add_node("extractor", extractor)
workflow.add_node("reconcile", reconcile)
workflow.add_node("validator", validator)
workflow.add_node("summary", generate_summary)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "extractor")
workflow.add_edge("extractor", "reconcile")
workflow.add_edge("reconcile", "validator")
workflow.add_edge("validator", "summary")

workflow.set_finish_point("summary")

graph = workflow.compile()


if __name__ == "__main__":

    pdf_path = r"data\patient_2\patient_2.pdf"

    try:

        images = pdf_to_images(pdf_path)

        print(f"\nFound {len(images)} pages")

        pdf_text = ""

        # OCR first 2 pages (Gemini free tier friendly)
        for image_path in images[:10]:

            print(f"Processing {image_path}")

            page_text = extract_page_text(image_path)

            pdf_text += page_text + "\n"

        print("\nOCR Extraction Complete")
        print(f"Characters Extracted: {len(pdf_text)}")

        print("\nFirst 500 characters:\n")
        print(pdf_text[:500])

    except Exception as e:

        print(f"PDF/OCR Error: {e}")
        exit()

    initial_state = {
        "pdf_path": pdf_path,
        "pdf_text": pdf_text,
        "extracted": False,
        "medications_extracted": False,
        "conflicts_detected": False,
    }

    try:

        result = graph.invoke(initial_state)

        print("\n========== FINAL OUTPUT ==========\n")

        os.makedirs("outputs", exist_ok=True)

        if "final_summary" in result:

            summary = result["final_summary"]

            print(summary)

            # Save TXT
            with open(
                "outputs/discharge_summary.txt",
                "w",
                encoding="utf-8"
            ) as f:
                f.write(summary)

            # Save JSON
            summary_json = {
                "generated_summary": summary
            }

            with open(
                "outputs/discharge_summary.json",
                "w",
                encoding="utf-8"
            ) as f:
                json.dump(
                    summary_json,
                    f,
                    indent=4,
                    ensure_ascii=False
                )

            # Save Reasoning Trace
            reasoning_trace = [
                {
                    "step": 1,
                    "action": "PDF OCR",
                    "result": f"{len(pdf_text)} characters extracted"
                },
                {
                    "step": 2,
                    "action": "Information Extraction",
                    "result": "Completed"
                },
                {
                    "step": 3,
                    "action": "Medication Reconciliation",
                    "result": "Completed"
                },
                {
                    "step": 4,
                    "action": "Validation",
                    "result": "Completed"
                },
                {
                    "step": 5,
                    "action": "Discharge Summary Generation",
                    "result": "Completed"
                }
            ]

            with open(
                "outputs/reasoning_trace.json",
                "w",
                encoding="utf-8"
            ) as f:
                json.dump(
                    reasoning_trace,
                    f,
                    indent=4
                )

            print("\nFiles saved successfully:")
            print("outputs/discharge_summary.txt")
            print("outputs/discharge_summary.json")
            print("outputs/reasoning_trace.json")

        else:
            print(result)

    except Exception as e:

        print(f"\nWorkflow Error: {e}")