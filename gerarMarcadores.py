from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

fig = plt.figure()
nx = 5
ny = 3
for i in range(1, nx*ny+1):
    ax = fig.add_subplot(ny,nx, 1)
    img = aruco.drawMarker(aruco_dict,i, 700)
    plt.imshow(img, cmap = mpl.cm.gray, interpolation="nearest")
    ax.axis("off")

plt.savefig("marker-Aruco_4x4_50.pdf")
plt.show()