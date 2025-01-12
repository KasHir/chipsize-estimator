from rectpack import newPacker
import matplotlib.pyplot as plt
import os

# ブロックデータ
blocks = [(5, 10), (5, 10), (8, 8), (8, 8), (6, 7), (4, 7), (15, 25),
          (5, 10), (5, 10), (8, 8), (8, 8), (6, 7), (4, 7), (15, 25)]  # (幅, 高さ)

# 最小チップサイズ探索
def find_minimum_chip_size_with_ids(blocks):
    # 初期値: 最大幅・高さの合計を仮の上限とする
    max_width = sum(block[0] for block in blocks)
    max_height = sum(block[1] for block in blocks)

    # 探索範囲の下限・上限
    min_size = max(max(block[0] for block in blocks), max(block[1] for block in blocks))  # 最小辺

    # 保存先ディレクトリ作成
    output_dir = "chip_layouts"
    os.makedirs(output_dir, exist_ok=True)

    # サイズを小さい方から探索
    for size in range(min_size, max(max_width, max_height) + 1):
        packer = newPacker()
        for i, block in enumerate(blocks):
            packer.add_rect(*block, rid=i)  # ブロックIDを追加
        print(f"try: {size} x {size}")
        packer.add_bin(size, size)  # 正方形ビンで探索
        packer.pack()

        # 成功した場合、結果を保存して終了
        if len(packer.rect_list()) == len(blocks):  # 全ブロックが配置可能
            # 探索中の配置結果を描画
            fig, ax = plt.subplots()
            for rect in packer.rect_list():
                x, y, w, h, rid = rect[1], rect[2], rect[3], rect[4], rect[5]
                ax.add_patch(plt.Rectangle((x, y), w, h, edgecolor='blue', facecolor='lightblue'))
                ax.text(x + w / 2, y + h / 2, str(rid), color='red', ha='center', va='center')  # IDを表示
            plt.xlim(0, size)
            plt.ylim(0, size)
            plt.gca().set_aspect('equal', adjustable='box')

            # ファイル名にサイズを付加して保存
            filename = os.path.join(output_dir, f"chip_layout_{size}.png")
            plt.savefig(filename)
            plt.close()

            print(f"Saved layout image: {filename}")
            return size, size  # 最小サイズを返す

    return None, None  # 配置できない場合

# 最小サイズ探索
chip_width, chip_height = find_minimum_chip_size_with_ids(blocks)

# 結果出力
if chip_width and chip_height:
    print(f"最小チップサイズ: {chip_width} x {chip_height}")
else:
    print("配置できるチップサイズが見つかりませんでした。")
