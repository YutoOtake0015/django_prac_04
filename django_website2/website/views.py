from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "yuto"
        return ctxt 
    
class AboutView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self):
        ctcx = super().get_context_data()
        ctcx["num_services"] = 999999
        ctcx["skills"] = {
            "Python", 
            "C++",
            "JavaScript", 
            "Rust", 
            "Go",
        }
        return ctcx