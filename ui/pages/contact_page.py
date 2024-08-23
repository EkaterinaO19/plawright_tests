from playwright.sync_api import Page, expect
from PIL import Image, ImageDraw
import io


class ContactPage:
    def __init__(self, page: Page):
        self.page = page
        self.name = page.get_by_placeholder("Name")
        self.email = page.get_by_placeholder("Email", exact=True)
        self.subject = page.get_by_placeholder("Subject")
        self.message = page.get_by_placeholder("Your Message Here")
        self.upload = page.locator("input[name=\"upload_file\"]")
        self.submit = page.get_by_role("button", name="Submit")
        self.dialog = page.once("dialog", lambda dialog: dialog.dismiss())
        self.success_msg = page.locator('.status alert alert-success')

        # Generate a fake image for testing
        self.fake_image_path = "fake_image.jpg"
        self.create_fake_image(self.fake_image_path)

        self.page.once("dialog", lambda dialog: dialog.dismiss())

    def create_fake_image(self, file_path):
        img = Image.new('RGB', (100, 100), color='white')
        d = ImageDraw.Draw(img)
        d.text((10, 10), "Fake Image", fill=(0, 0, 0))
        img.save(file_path)

    def upload_file(self):
        self.upload.set_input_files(self.fake_image_path)

    def submit_form(self):
        self.submit.click()

    def verify_success(self):
        return self.success_msg.inner_text()
