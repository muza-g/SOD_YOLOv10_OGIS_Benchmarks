from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import json
import argparse

def load_coco_data(ground_truth_path, predictions_path):
    """Loads COCO Ground Truth and Predictions."""
    print("Loading Ground Truth from:", ground_truth_path)
    coco_gt = COCO(ground_truth_path)
    print("Loading Predictions from:", predictions_path)
    coco_pred = coco_gt.loadRes(predictions_path)
    return coco_gt, coco_pred

def evaluate_coco(coco_gt, coco_pred):
    """Evaluates predictions using COCO Evaluation metrics."""
    print("Evaluating...")
    coco_eval = COCOeval(coco_gt, coco_pred, iouType='bbox')
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Evaluate COCO predictions against ground truth.")
    parser.add_argument("--ground_truth_path", required=True, help="Path to the COCO ground truth JSON file.")
    parser.add_argument("--predictions_path", required=True, help="Path to the COCO predictions JSON file.")
    args = parser.parse_args()

    try:
        # Load Data
        coco_gt, coco_pred = load_coco_data(args.ground_truth_path, args.predictions_path)

        # Evaluate
        evaluate_coco(coco_gt, coco_pred)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
