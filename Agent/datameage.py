from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False) # Set to True to enable plugins
md = MarkItDown(docintel_endpoint="<document_intelligence_endpoint>")
result = md.convert("周三甫个人简历_pub.pdf")
print(result.text_content)