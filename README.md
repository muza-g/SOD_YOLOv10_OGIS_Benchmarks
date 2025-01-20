
# Advancing Small Object Detection in UAV Imagery: A Two-Stage Framework Leveraging YOLOv10 and Object Guided Inference Slicing (OGIS) on the VisDrone Dataset

## Description
*(To be added later)*

---

## Testing Code Steps

1. **Download Required Files**:
   - **Ground Truth (GT)**: Download the COCO.json file containing the ground truth annotations.
   - **FI-Det COCO.json**: Download the Full Inference Detection results in COCO.json format.
   - **OGIS-Det COCO.json**: Download the Object Guided Inference Slicing Detection results in COCO.json format.
   - Upload the files to your preferred storage location (e.g., Google Drive).

2. **Evaluation Steps**:
   - **FI-Det Evaluation**:
     ```bash
     python _Evaluation_coco_results.py --GT-path="<path_to_GT.json>" --FI-Det_COCO.json-path="<path_to_FI-Det.json>"
     ```
   - **OGIS-Det Evaluation**:
     ```bash
     python _Evaluation_coco_results.py --GT-path="<path_to_GT.json>" --OGIS-Det_COCO.json-path="<path_to_OGIS-Det.json>"
     ```
   - **Comparison of FI-Det and OGIS-Det**:
     ```bash
     python Compare_FI-Det_AND_OGIS-Det.py
     ```
   - **Upscale and Compare**:
     ```bash
     python Upscale_AND_Compare.py
     ```

---

## Part 1: NOT Fine-Tuned (NFT) YOLOv10, Results are saved in **COCO.json** format.  
**Inference Experiment on 100% VisDrone2019 Train Dataset (6,471 Images)**

-  [**Ground Truth (GT)**:](https://drive.google.com/file/d/1-xQ6z7Yx0y3pZp_TZpbWjbM4VrbQ4yL0/view?usp=drive_link)  - [**Full Inference Detection (FI-Det)**:](https://drive.google.com/file/d/108lw39DbQaNFfLH4hRiXDUPBHN0aMwoq/view?usp=drive_link)  -  [**Object Guided Inference Slicing Detection (OGIS-Det)**:](https://drive.google.com/file/d/10Br73D63gjm_w4EH9IxREcNnS6yM0H0v/view?usp=drive_link)


### Evaluation Table: YOLOv10 FI-Det vs. GOIS-Det

| **Metric**                                   | **AP@[IoU=0.50:0.95]** | **AP@[IoU=0.50]** | **AP@[IoU=0.75]** | **AP@[IoU=0.50] Small** | **AP@[IoU=0.50] Medium** | **AP@[IoU=0.50] Large** | **AR@[IoU=0.50:0.95] MaxDets=1** | **AR@[IoU=0.50:0.95] MaxDets=10** | **AR@[IoU=0.50:0.95] MaxDets=100** | **AR@[IoU=0.50] Small** | **AR@[IoU=0.50] Medium** | **AR@[IoU=0.50] Large** |
|---------------------------------------------|-------------------------|-------------------|-------------------|-------------------------|--------------------------|--------------------------|-----------------------------------|-----------------------------------|-----------------------------------|--------------------------|--------------------------|--------------------------|
| **FI-Det**                                  | 0.011                   | 0.015             | 0.011             | 0.002                   | 0.018                    | 0.06                     | 0.011                             | 0.024                             | 0.025                             | 0.003                    | 0.035                    | 0.12                     |
| **OGIS-Det**                                | 0.03                    | 0.045             | 0.032             | 0.008                   | 0.052                    | 0.097                    | 0.025                             | 0.06                              | 0.075                             | 0.029                    | 0.124                    | 0.189                    |
| **% Improve**                               | ↑ 184.99%              | ↑ 192.79%         | ↑ 183.78%         | ↑ 407.04%              | ↑ 194.20%               | ↑ 62.68%                | ↑ 121.36%                         | ↑ 154.18%                         | ↑ 199.64%                         | ↑ 833.35%               | ↑ 252.87%               | ↑ 57.76%                |

---

## Part 2: NOT Fine-Tuned (NFT) YOLOv10  
**Inference Experiment on 15% VisDrone2019 Train Dataset (970 Images) AND Available Data:Results are saved in **COCO.json** format
-  [**Ground Truth (GT)**:](https://drive.google.com/file/d/1kFNr8s_Yg0Yb0xxXuF4awaIWCwpehGTZ/view?usp=drive_link)  [**Full Inference Detection (FI-Det)**:](https://drive.google.com/file/d/1VuiYajOY6k4bFt6Crp5W4sZGAMy-g8dm/view?usp=drive_link)   [**Object Guided Inference Slicing Detection (OGIS-Det)**:](https://drive.google.com/file/d/1aETLjqsbbtoTAeA0kmNUAa0TnbDfSwiT/view?usp=drive_link)

## Evaluation Table: YOLOv10 FI-Det vs. GOIS-Det

The following table compares **Full Inference Detection (FI-Det)** and **Object Guided Inference Slicing Detection (OGIS-Det)** for YOLOv10, along with the percentage improvement achieved by OGIS-Det over FI-Det.

| **Metric**           | **mAP-Small** | **AR-Small** | **mAP-Medium** | **mAP-Large** | **AR@1** | **AR@10** | **AR@100** | **AR-Medium** | **AR-Large** | **F1 Score** | **mAP@0.50:0.95** | **mAP@0.50** | **mAP@0.75** |
|-----------------------|---------------|---------------|----------------|---------------|-----------|-----------|------------|---------------|--------------|--------------|-------------------|-------------|--------------|
| **FI-Det**           | 0.02          | 0.02          | 0.18           | 0.63          | 0.13      | 0.25      | 0.27       | 0.38          | 1.18         | 0.17         | 0.12              | 0.17        | 0.13         |
| **OGIS-Det**         | 0.08          | 0.27          | 0.56           | 0.93          | 0.26      | 0.61      | 0.76       | 1.25          | 1.85         | 0.44         | 0.31              | 0.48        | 0.33         |
| **% Improve**        | ↑ 300.0%      | ↑ 1250.0%     | ↑ 211.11%      | ↑ 47.62%      | ↑ 100.0%  | ↑ 144.0%  | ↑ 181.48%  | ↑ 228.95%     | ↑ 56.78%     | ↑ 158.82%    | ↑ 158.33%         | ↑ 182.35%   | ↑ 153.85%    |

---

### Observations
- **Significant Improvements**: The OGIS-Det framework consistently outperformed FI-Det across all metrics, with particularly substantial improvements in **AR-Small** (+1250.0%) and **mAP-Small** (+300.0%).
- **Detection Accuracy**: Notable increases in **mAP@0.50** (+182.35%) and **mAP@0.75** (+153.85%) indicate better performance across various IoU thresholds.
- **Enhanced Recall**: Improvements in **AR@100** (+181.48%) and **AR-Medium** (+228.95%) highlight OGIS-Det's ability to enhance recall, particularly for medium-sized objects.

---

## Part 3: Fine-Tuned (FT) YOLOv10 
**Trained for 10 Epochs on 100% VisDrone2019 Train Dataset (6,471 Images) and Inference on the Same Dataset, Results are saved in **COCO.json** format.**
- [**Ground Truth (GT)**: ](https://drive.google.com/file/d/15KjnH9FoEfxb9ZnIOjPPMwGsPgxC7Yfu/view?usp=drive_link)  [ **Full Inference Detection (FI-Det)**:](https://drive.google.com/file/d/1-5xldi9gBTT6Qwm-vcj8JjqJMSIloFwh/view?usp=drive_link)   [**Object Guided Inference Slicing Detection (OGIS-Det)**:](https://drive.google.com/file/d/1-6odgDZHwtGsFqFrgeFfTmyTkL34aZWD/view?usp=drive_link)


### Evaluation Table: YOLOv10 FI-Det vs. GOIS-Det

The following table compares **Full Inference Detection (FI-Det)** and **Object Guided Inference Slicing Detection (OGIS-Det)** for YOLOv10, along with the percentage improvement achieved by OGIS-Det over FI-Det.

| **Metric**           | **AP-Small** | **AR-Small** | **AP-Medium** | **AP-Large** | **AR@1** | **AR@10** | **AR@100** | **AR-Medium** | **AR-Large** | **F1 Score** | **AP@[IoU=0.50:0.95]** | **AP@[IoU=0.50]** | **AP@[IoU=0.75]** |
|-----------------------|--------------|--------------|---------------|--------------|-----------|-----------|------------|---------------|--------------|--------------|------------------------|------------------|------------------|
| **FI-Det**           | 0.022        | 0.029        | 0.133         | 0.222        | 0.041     | 0.097     | 0.117      | 0.178         | 0.278        | 0.17         | 0.091                 | 0.140            | 0.100            |
| **OGIS-Det**         | 0.061        | 0.110        | 0.130         | 0.101        | 0.047     | 0.127     | 0.171      | 0.218         | 0.159        | 0.44         | 0.099                 | 0.156            | 0.107            |
| **% Improve**        | ↑ 176.54%    | ↑ 279.22%    | ↓ 2.30%       | ↓ 54.85%     | ↑ 14.18%  | ↑ 31.01%  | ↑ 46.09%   | ↑ 22.50%      | ↓ 42.82%     | ↑ 158.82%    | ↑ 8.88%               | ↑ 11.40%         | ↑ 7.08%          |

---

### Observations
- **Improvements**:
  - **AP-Small** and **AR-Small** saw significant improvements of **+176.54%** and **+279.22%**, respectively.
  - **AR@100** and **AR@10** improved by **46.09%** and **31.01%**, respectively.
- **Decreased Metrics**:
  - **AP-Large** and **AR-Large** decreased by **54.85%** and **42.82%**, respectively, suggesting a potential trade-off in performance for larger objects.

This analysis highlights the strengths of the OGIS-Det framework in improving small object detection while identifying areas for potential optimization in large object detection scenarios.

---

## Citation
If you use this framework or dataset in your research, please cite this work:
```bibtex
@article{yourpaper2025,
  title={Advancing Small Object Detection in UAV Imagery: A Two-Stage Framework Leveraging YOLOv10 and Object Guided Inference Slicing (OGIS) on the VisDrone Dataset},
  author={Your Name and Co-Authors},
  year={2025},
  journal={Your Journal Name},
  publisher={Your Publisher},
}
```

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements
We acknowledge the creators of the **VisDrone2019** dataset and contributors to the **YOLOv10** framework.
```

---

