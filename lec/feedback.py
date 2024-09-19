import qrcode
from matplotlib import pyplot as plt

def feedback():
    return

def _feedback():
    # TODO read once we have new feedback link
    FEEDBACK_URL = "https://go.blueja.io/BeQtMbSiPUm6DWQUJ2WVgA"
    qr = qrcode.make(FEEDBACK_URL)

    plt.title("Module feedback now open!")
    plt.imshow(qr, cmap="Greys_r")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # feedback()
    pass
