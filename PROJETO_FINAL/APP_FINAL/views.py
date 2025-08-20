from django.shortcuts import render, redirect, get_object_or_404
from .models import CarrosselSlide, Produto, SecaoSobre

def pagina_inicial(request):
    slides_carrossel = CarrosselSlide.objects.all()
    produtos = Produto.objects.all()
    secao_sobre = SecaoSobre.objects.first()

    contexto = {
        'slides_carrossel': slides_carrossel,
        'produtos': produtos,
        'secao_sobre': secao_sobre,
    }
    return render(request, 'home.HTML', contexto)

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho = request.session.get('carrinho', {})
    
    item_carrinho = carrinho.get(str(produto_id))
    
    if item_carrinho:
        item_carrinho['quantidade'] += 1
    else:
        carrinho[str(produto_id)] = {
            'quantidade': 1,
            'preco': str(produto.preco),
            'nome': produto.nome,
            'url_imagem': produto.imagem.url if produto.imagem else ''
        }
    
    request.session['carrinho'] = carrinho
    return redirect('pagina_inicial')

def remover_do_carrinho(request, produto_id):
    carrinho = request.session.get('carrinho', {})
    
    if str(produto_id) in carrinho:
        if carrinho[str(produto_id)]['quantidade'] > 1:
            carrinho[str(produto_id)]['quantidade'] -= 1
        else:
            del carrinho[str(produto_id)]
    
    request.session['carrinho'] = carrinho
    return redirect('pagina_inicial')

def ver_carrinho_modal(request):
    carrinho = request.session.get('carrinho', {})
    preco_total = sum(float(item['preco']) * item['quantidade'] for item in carrinho.values())
    
    contexto = {
        'carrinho': carrinho,
        'preco_total': preco_total
    }
    return render(request, 'carrinho_modal_conteudo.html', contexto)