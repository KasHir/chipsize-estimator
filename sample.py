from rectpack import newPacker
import matplotlib.pyplot as plt

# IPブロックデータ
blocks = [(5, 10),(5, 10), (8, 8),(8, 8), (6, 7),(4, 7),(15,25)]  # (幅, 高さ)
bin_size = (30, 30)  # チップサイズ

# パッカー初期化
packer = newPacker()

# ブロックとビン追加
for block in blocks:
    packer.add_rect(*block)
packer.add_bin(*bin_size)

# パッキング実行
packer.pack()

# 結果表示
for rect in packer.rect_list():
    print(f"Block {rect[4]} placed at {rect[1]}, {rect[2]} with size {rect[3]}x{rect[4]}")



# 配置結果描画
fig, ax = plt.subplots()
for rect in packer.rect_list():
    x, y, w, h = rect[1], rect[2], rect[3], rect[4]
    ax.add_patch(plt.Rectangle((x, y), w, h, edgecolor='blue', facecolor='lightblue'))
plt.xlim(0, bin_size[0])
plt.ylim(0, bin_size[1])

plt.savefig("chip_layout.png", dpi=300)
