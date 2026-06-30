class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filmes = Filme.objects.all()

        context["filme_destaque"] = filmes.first()
        context["lista_filmes_recentes"] = filmes
        context["lista_filmes_emalta"] = filmes.order_by("-visualizacoes")

        return context