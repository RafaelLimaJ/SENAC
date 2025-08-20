def contexto_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    quantidade_itens_carrinho = sum(item['quantidade'] for item in carrinho.values())
    return {
        'quantidade_itens_carrinho': quantidade_itens_carrinho
    }