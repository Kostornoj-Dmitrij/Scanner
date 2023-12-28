import unittest
import fitz  # PyMuPDF
from PIL import Image, ImageChops

class MyTestCase(unittest.TestCase):
    def test_get_link(self):
        result = get_link()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("http"))
    def test_send_link(self):
        link = "http://example.com"
        result = send_link(link)
        self.assertEqual(result, "Link sent successfully")

    def test_compare_same_images_pdfs(self):
        pdf_document = "test_same_images.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_same_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_different_images_pdfs(self):
        pdf_document = "test_different_images.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_different_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertNotEqual(diff.getbbox(), None)

    def test_compare_empty_pdf(self):
        pdf_document = "test_empty.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_empty_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_single_page_pdfs(self):
        pdf_document = "test_single_page.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_empty_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_multi_page_pdfs(self):
        pdf_document = "test_multi_page_image.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        page2 = doc.load_page(1)
        img1 = page1.get_pixmap() + page2.get_pixmap()
        img2 = Image.open("expected_multi_page_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_large_pdfs(self):
        pdf_document = "test_large_image.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        page2 = doc.load_page(1)
        img1 = page1.get_pixmap() + page2.get_pixmap()
        img2 = Image.open("expected_large_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_corrupted_pdfs(self):
        pdf_document = "test_corrupted_image.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_corrupted_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_invalid_pdfs(self):
        pdf_document = "test_invalid_image.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_invalid_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_mixed_content_pdfs(self):
        pdf_document = "test_mixed_content_image.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_mixed_content_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_high_resolution_pdfs(self):
        pdf_document = "test_high_resolution_image.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_high_resolution_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_low_resolution_pdfs(self):
        pdf_document = "test_low_resolution_image.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_low_resolution_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_with_alpha_channel_pdfs(self):
        pdf_document = "test_alpha_channel_images.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_alpha_channel_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.mode, 'RGBA')

    def test_compare_black_and_white_images_pdfs(self):
        pdf_document = "test_black_and_white_image.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_black_and_white_image.png").convert('1')
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_grayscale_images_pdfs(self):
        pdf_document = "test_grayscale_image.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_grayscale_image.png").convert('L')
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_with_threshold_pdfs(self):
        pdf_document = "test_threshold_images.pdf"
        doc = fitz.open(pdf_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_threshold_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        threshold = 50
        self.assertLessEqual(diff.getbbox(), threshold)

    def test_compare_same_images_docs(self):
        doc_document = "test_same_images.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_same_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_different_images_docs(self):
        doc_document = "test_different_images.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_different_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertNotEqual(diff.getbbox(), None)

    def test_compare_empty_doc(self):
        doc_document = "test_empty.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_empty_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_single_page_docs(self):
        doc_document = "test_single_page.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_empty_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_multi_page_docs(self):
        doc_document = "test_multi_page_image.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        page2 = doc.load_page(1)
        img1 = page1.get_pixmap() + page2.get_pixmap()
        img2 = Image.open("expected_multi_page_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_large_docs(self):
        doc_document = "test_large_image.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        page2 = doc.load_page(1)
        img1 = page1.get_pixmap() + page2.get_pixmap()
        img2 = Image.open("expected_large_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_corrupted_docs(self):
        doc_document = "test_corrupted_image.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_corrupted_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_invalid_docs(self):
        doc_document = "test_invalid_image.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_invalid_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_mixed_content_docs(self):
        doc_document = "test_mixed_content_image.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_mixed_content_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_high_resolution_docs(self):
        doc_document = "test_high_resolution_image.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_high_resolution_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_low_resolution_docs(self):
        doc_document = "test_low_resolution_image.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_low_resolution_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_with_alpha_channel_docs(self):
        doc_document = "test_alpha_channel_images.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_alpha_channel_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.mode, 'RGBA')

    def test_compare_black_and_white_images_docs(self):
        doc_document = "test_black_and_white_image.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_black_and_white_image.png").convert('1')
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_grayscale_images_docs(self):
        doc_document = "test_grayscale_image.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_grayscale_image.png").convert('L')
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_with_threshold_docs(self):
        doc_document = "test_threshold_images.doc"
        doc = fitz.open(doc_document)
        page1 = doc.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_threshold_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        threshold = 50
        self.assertLessEqual(diff.getbbox(), threshold)
        
    def test_compare_same_images_xlss(self):
        xls_xlsument = "test_same_images.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_same_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_different_images_xls(self):
        xls_xlsument = "test_different_images.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_different_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertNotEqual(diff.getbbox(), None)

    def test_compare_empty_xls(self):
        xls_xlsument = "test_empty.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_empty_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_single_page_xls(self):
        xls_xlsument = "test_single_page.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_empty_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_multi_page_xls(self):
        xls_xlsument = "test_multi_page_image.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        page2 = xls.load_page(1)
        img1 = page1.get_pixmap() + page2.get_pixmap()
        img2 = Image.open("expected_multi_page_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_large_xls(self):
        xls_xlsument = "test_large_image.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        page2 = xls.load_page(1)
        img1 = page1.get_pixmap() + page2.get_pixmap()
        img2 = Image.open("expected_large_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_corrupted_xls(self):
        xls_xlsument = "test_corrupted_image.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_corrupted_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_invalid_xls(self):
        xls_xlsument = "test_invalid_image.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_invalid_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_mixed_content_xls(self):
        xls_xlsument = "test_mixed_content_image.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_mixed_content_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_high_resolution_xls(self):
        xls_xlsument = "test_high_resolution_image.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_high_resolution_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)


    def test_compare_low_resolution_xls(self):
        xls_xlsument = "test_low_resolution_image.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_low_resolution_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_with_alpha_channel_xls(self):
        xls_xlsument = "test_alpha_channel_images.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_alpha_channel_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.mode, 'RGBA')

    def test_compare_black_and_white_images_xls(self):
        xls_xlsument = "test_black_and_white_image.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_black_and_white_image.png").convert('1')
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_grayscale_images_xls(self):
        xls_xlsument = "test_grayscale_image.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_grayscale_image.png").convert('L')
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        self.assertEqual(diff.getbbox(), None)

    def test_compare_with_threshold_xls(self):
        xls_xlsument = "test_threshold_images.xls"
        xls = fitz.open(xls_xlsument)
        page1 = xls.load_page(0)
        img1 = page1.get_pixmap()
        img2 = Image.open("expected_threshold_image.png")
        diff = ImageChops.difference(Image.frombytes("RGB", img1.size, img1.samples), img2)
        threshold = 50
        self.assertLessEqual(diff.getbbox(), threshold)

if __name__ == '__main__':
    unittest.main()
