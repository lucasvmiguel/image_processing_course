from cv2 import cv2
from skimage import io

image = io.imread(
    "https://s2.glbimg.com/LLxhaPRsM5Mn6lhVv3wlzNG0ODc=/206x116/top/smart/filters:strip_icc()/s2.glbimg.com/8mO5ljmoOlL53O4BRt012IMfmsE=/0x79:2181x1304/267x150/i.s3.glbimg.com/v1/AUTH_bc8228b6673f488aa253bbcb03c80ec5/internal_photos/bs/2019/C/A/Da8pXuSsebbDI8BqFW9w/2019-06-15t130710z-627885851-rc1929621690-rtrmadp-3-soccer-worldcup-nld-cmr.jpg"
)

cv2.imshow("Original", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))


cv2.waitKey(5000)
