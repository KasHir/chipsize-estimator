from rectpack import newPacker
import matplotlib.pyplot as plt

# IPブロックデータ
blocks = [(5, 10),(5, 10), (8, 8),(8, 8), (6, 7),(4, 7),(15,25)]  # (幅, 高さ)

# 最小チップサイズ探索
def find_minimum_chip_size(blocks):
    # 初期値: 最大幅・高さの合計を仮の上限とする
    max_width = sum(block[0] for block in blocks)
    max_height = sum(block[1] for block in blocks)
    
    # 探索範囲の下限・上限
    min_size = max(max(block[0] for block in blocks), max(block[1] for block in blocks))  # 最小辺
    best_width, best_height = max_width, max_height
    
    # サイズを縮小しながら探索
    for size in range(min_size, max(max_width, max_height) + 1):
        packer = newPacker()
        for block in blocks:
            packer.add_rect(*block)
        packer.add_bin(size, size)  # 正方形ビンで探索
        packer.pack()
        
        # 成功した場合、最適なサイズを更新
        if len(packer.rect_list()) == len(blocks):  # 全ブロックが配置可能
            best_width, best_height = size, size
            break

    return best_width, best_height, packer

# 最小サイズ探索
chip_width, chip_height, final_packer = find_minimum_chip_size(blocks)

# 結果表示
print(f"最小チップサイズ: {chip_width} x {chip_height}")
for rect in final_packer.rect_list():
    print(f"Block placed at {rect[1]}, {rect[2]} with size {rect[3]}x{rect[4]}")

# 配置結果描画
fig, ax = plt.subplots()
for rect in final_packer.rect_list():
    x, y, w, h = rect[1], rect[2], rect[3], rect[4]
    ax.add_patch(plt.Rectangle((x, y), w, h, edgecolor='blue', facecolor='lightblue'))
plt.xlim(0, chip_width)
plt.ylim(0, chip_height)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()


plt.savefig("chip_layout.png", dpi=300)
