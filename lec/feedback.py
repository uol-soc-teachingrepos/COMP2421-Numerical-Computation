import qrcode
from matplotlib import pyplot as plt


def feedback():
    FEEDBACK_URL = "https://leeds.bluera.com/leeds/"
    qr = qrcode.make(FEEDBACK_URL)

    plt.title("Module feedback now open!")
    plt.imshow(qr, cmap="Greys_r")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # feedback()
    pass
