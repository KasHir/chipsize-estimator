# **Chip Size Estimator**

This project calculates the minimum square chip size needed to fit a set of rectangular blocks and visualizes the layout with block IDs.

---

## **Features**
- Calculates the minimum chip size for given blocks.
- Saves layout images with block IDs in the `chip_layouts` folder.

---

## **Requirements**
- Python 3.7+
- Libraries: `rectpack`, `matplotlib`

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## **Usage**
1. Define block dimensions in the `blocks` list in the script:
   ```python
   blocks = [(5, 10), (8, 8), (6, 7), (15, 25)]
   ```

2. Run the script:
   ```bash
   python chip_size_estimator.py
   ```

3. Outputs:
   - Minimum chip size printed in the console.
   - Layout images saved in `chip_layouts`.

---

## **Example Output**
Console:
```
Trying: 28 x 28
Saved layout image: chip_layouts/chip_layout_28.png
Minimum chip size: 28 x 28
```

Generated Image:
- Blocks are visualized with their IDs.

---

## **License**
This project is licensed under the MIT License.

--- 

This version is concise and focuses on essential details.