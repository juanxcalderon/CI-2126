import re
import check50

@check50.check()
def exists():
    """README.md existe"""
    check50.exists("README.md")

@check50.check(exists)
def final():
    """detalles del proyecto final"""
    text = open("README.md").read().lower()
    if len(text) < 2500:
        raise check50.Failure(f"La descripción no es lo suficientemente larga.")
       
    urls = re.findall('https?:\/\/[\w/\-?=%.]+\.[\w/\-?=%.]+', text)
    if not urls:
        raise check50.Failure(f"El URL del video no se encuentra.")
        
