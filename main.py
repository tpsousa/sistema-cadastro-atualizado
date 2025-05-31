from function import *
#funcao de criar menu

missao = [];

def menu():
    while True:
        print("seja bem vindo a pagina de cadastro");
        print("1.cadastrar missao");
        print("2.listar missoes");
        print("3.simular lancamento");
        print("4.sair")

        opcao = input("digite sua opcao escolhida: ");
        
        if opcao == '1':
         cadastrarMissao(missao);
       
        elif opcao == '2':
         listarMissoes(missao);
      
        elif opcao =='3':
          simularLancamento(missao);
          
        elif opcao == '4':
           print("saindo...")
           break;
           
        else:
           print("opcao invalida");

menu();
        
        

        

    