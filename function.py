
def cadastrarMissao(list):
  nave = input("say the name of ur ship");
  destiny  = input("write the name of ur destiny");
  quantity_people = int(input("say the quantity of people in the nave"))
  fuel = float(input("say the quantity of fuel in ur nave"));
  time_days = int(input("say the quantity days of ur trip"))

  missao = {
    "nave" : nave,
    "destiny" : destiny,
    "quantity_people" : quantity_people,
    "fuel" : fuel,
    "time_days" : time_days
  }
  
  list.append(missao)
  print("missao cadastrada com sucesso");

def listarMissoes(list):
  if len(list)==0:
     print("nao ha missoes cadastradas");
     return
  else:
    for indice,missao in enumerate(list):
      print(f"missao{indice + 1}");
      print(f"{missao['nave']} (nome da nave)");
      print(f"{missao['destiny']} (destino)");
      print(f"{missao['quantity_people']} (quantidade de tripulantes)");
      print(f"{missao['fuel']} (fuel)");
      print(f"{missao['time_days']} (quantidade de dias)");

def simularLancamento(list):
  if len(list)==0:
    print("dont exists missions in ur list")
    return;
  
  for indice,missao in enumerate(list):
    print(f"{indice + 1} - {missao['nave']} - {missao['quantity_people']}")
      
    
  escolha = int(input("choose ur mission")) - 1;

  if 0 <= escolha <= len(list):
    missao = list[escolha];

    missao['tripulantes'];


      
    quantity_max = missao['quantity_people'] * 500;
      
    if missao['fuel'] >= quantity_max:
        print("mission launched with sucess");
    else:
        print("mission failed");
  else:
      print("invalid option");

  
print("teste");