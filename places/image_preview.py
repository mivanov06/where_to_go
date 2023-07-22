from django.utils.html import format_html


def image_preview(image):
    height = 300
    return format_html(
        "<img src={} height={} />",
        image.image.url,
        height,
    )
