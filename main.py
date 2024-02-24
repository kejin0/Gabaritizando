from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager,Screen,SlideTransition
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.utils import get_color_from_hex
from kivy.metrics import dpi2px
from kivy.uix.stacklayout import StackLayout
import time

#Window.size = (360, 800)
Window.clearcolor = get_color_from_hex("#fe97b0")

class Textinhodeerro(Label):
    pass

class Comecar(Screen):
    def erro(self):
        self.add_widget(Textinhodeerro(pos_hint={"center_x":.5,"y":.752}))

class Inicial(Screen):
    pass

class Prova1(Screen):
    pass


class Prova2(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class Titulo(Widget):
    def texto(self):
        return "Gabaritando"

class Entradadetexto(TextInput):
    pass



class Submit(Button):
    pass

class Botao_do_sumario(Button):
    pass

class Sumario(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        num = 1
        for i in range(1,91):
            bt = Botao_do_sumario()
            bt.text = str(num)
            self.add_widget(bt)
            num += 1

class Alternativa(Button):
    pass

class GabarizandoApp(App):
    nome = StringProperty()
    numero = NumericProperty()
    numero_ = NumericProperty()
    indice_questao = NumericProperty()
    texto_indice = StringProperty()
    gabarito_incorreto_formatado = StringProperty()
    numero_de_acertos = NumericProperty()
    numero_de_acertos_formatado = StringProperty()
    cora = ListProperty()
    corb = ListProperty()
    corc = ListProperty()
    cord = ListProperty()
    core = ListProperty()


    def build(self):
       self.definicoes()
       self.desempenho()
       return Builder.load_file('kivyfiles.kv')


    def desempenho(self):
        bk = open("backup.txt",'r')
        linhas = bk.readlines()
        indice = len(linhas) - 1

        self.celula1 = ""
        self.celula2 = ""
        self.celula3 = ""
        self.celula4 = ""
        self.celula5 = ""
        self.celula6 = ""

        if indice != 0:
            print(linhas)
            celula1 = linhas[indice]
            celula1 = celula1.split("-MCPS-")
            self.celula1 = "{} -- {}".format(celula1[1],celula1[2])
            if indice >= 1:
                celula2 = linhas[indice - 1]
                celula2 = celula2.split("-MCPS-")
                self.celula2 = "{} -- {}".format(celula2[1],celula2[2])
                if indice >= 2:
                    celula3 = linhas[indice - 2]
                    celula3 = celula3.split("-MCPS-")
                    self.celula3 = "{} -- {}".format(celula3[1],celula3[2])
                    if indice >= 3:
                        celula4 = linhas[indice - 3]
                        celula4 = celula4.split("-MCPS-")
                        self.celula4 = "{} -- {}".format(celula4[1],celula4[2])
                        if indice >= 4:
                            celula5 = linhas[indice - 4]
                            celula5 = celula5.split("-MCPS-")
                            self.celula5 = "{} -- {}".format(celula5[1],celula5[2])
                            if indice >= 5:
                                celula6 = linhas[indice - 5]
                                celula6 = celula6.split("-MCPS-")
                                self.celula6 = "{} -- {}".format(celula6[1],celula6[2])

    def definicoes(self):
        self.definircores()
        self.indice_questao = 1
        self.texto_indice = f"Questão {self.indice_questao}"
        self.numero_de_questao = 90

        self.gabarito_pessoal = []
        for numero in range(1, 91):
            self.gabarito_pessoal.append("")
        self.gabarito_incorreto = []
        self.gabarito_oficial = []
        self.nome = ''
        self.gab_oficial_entrada = ""
    def definircores(self):
        self.color_base_botao = get_color_from_hex("#ffc3c3")
        self.cora = self.color_base_botao
        self.corb = self.color_base_botao
        self.corc = self.color_base_botao
        self.cord = self.color_base_botao
        self.core = self.color_base_botao

        self.cor1 = get_color_from_hex("#fd6906")
        self.cor2 = get_color_from_hex("#ffd47e")
        self.cor3 = get_color_from_hex("#ff867d")
        self.cor4 = get_color_from_hex("#ff9c95")
        self.cor5 = get_color_from_hex("#ffdadf")
        self.cor6 = get_color_from_hex("#fc7167")
        self.cor7 = get_color_from_hex("#ff8f44")
        self.cor8 = get_color_from_hex("#f41958")
        self.cor9 = get_color_from_hex("#fc7167")
        self.cor10 = get_color_from_hex("#fdb207")

    def extrairnome(self,texto_escrito):
        self.nome = texto_escrito

    def dpforpx(self,dp):
        return dpi2px(dp, 'dp')

    def ir(self,numero):
        self.indice_questao = int(numero)
        self.texto_indice = f"Questão {self.indice_questao}"

    def avancar(self):
        if self.indice_questao  <= self.numero_de_questao - 1:
            self.indice_questao += 1
            self.texto_indice = f"Questão {self.indice_questao}"

    def voltar(self):
        if self.indice_questao > 1:
            self.indice_questao -= 1
            self.texto_indice = f"Questão {self.indice_questao}"

    def assinalar(self,letra):
        self.gabarito_pessoal.pop(self.indice_questao - 1)
        self.gabarito_pessoal.insert(self.indice_questao - 1,letra)

    def tamanho(self,texto):
        texto = list(texto)
        self.gabarito_oficial = texto
        return str(len(texto))

    def correcao(self):
        if self.gabarito_oficial != []:
            for numero in range(0,len(self.gabarito_oficial)):
                if self.gabarito_pessoal[numero] != self.gabarito_oficial[numero]:
                    self.gabarito_incorreto.append(f"{self.ajeitarnumero(numero + 1)} - {self.gabarito_pessoal[numero]} - {self.gabarito_oficial[numero]}")
            self.gabarito_incorreto_formatado = str(self.gabarito_incorreto).replace("', '","\n").replace("['","").replace("']","")
            #print(self.gabarito_incorreto_formatado)
            self.numero_de_acertos = (len(self.gabarito_oficial) - len(self.gabarito_incorreto))
            self.numero_de_acertos_formatado = f"{self.numero_de_acertos}/{len(self.gabarito_oficial)}"
        else: pass

    def resetar(self):
        self.definicoes()

    def salvar_como_concluido(self):
        self.dados_guardar = f"-MCPS-{self.nome}-MCPS-{self.numero_de_acertos_formatado}-MCPS-{self.compactacao(self.gabarito_pessoal)}-MCPS-{self.compactacao(self.gabarito_oficial)}-MCPS-{self.indice_questao + 1}\n"
        bk = open("backup.txt", "r")
        if "RESUME" in bk.read():
            bk = open("backup.txt", "r")
            fatia = bk.read().split("RESUME")[0]
            bk.close()
            bk = open("backup.txt", "w")
            bk.write(fatia)
            bk.close()
            bk = open("backup.txt", "a")
            bk.write(f"COMPLETE{self.dados_guardar}")
            bk.close()


    def resume(self):
        bk = open("backup.txt", "r")
        linhas = bk.read().split("\n")
        ultima_linha = linhas[len(linhas) - 2]
        bk.close()
        if len(ultima_linha) >= 5 and "RESUME" in ultima_linha:
            ultima_linha_lista = ultima_linha.split("-MCPS-")
            gabarito_pessoal_velho = list(ultima_linha_lista[3])
            for i in range(0,90 - len(gabarito_pessoal_velho)):
                gabarito_pessoal_velho.append(" ")
            self.gabarito_pessoal = gabarito_pessoal_velho
            self.indice_questao = int(ultima_linha_lista[5])
            self.texto_indice = f"Questão {self.indice_questao}"
            self.ta_marcado()
            bk.close()
            self.pode_resumir = True
        else:self.pode_resumir = False

    def atualizar(self):
        self.dados_guardar = f"-MCPS-{self.nome}-MCPS-{self.numero_de_acertos_formatado}-MCPS-{self.compactacao(self.gabarito_pessoal)}-MCPS-{self.compactacao(self.gabarito_oficial)}-MCPS-{self.indice_questao + 1}\n"
        bk = open("backup.txt", "r")
        if "RESUME" in bk.read():
            bk = open("backup.txt", "r")
            fatia = bk.read().split("RESUME")[0]
            print(fatia)
            bk.close()
            bk = open("backup.txt", "w")
            bk.write(fatia)
            bk.close()
            bk = open("backup.txt", "a")
            bk.write(f"RESUME{self.dados_guardar}")
            bk.close()
        else:
            bk = open("backup.txt", "a")
            bk.write(f"RESUME{self.dados_guardar}")
            bk.close()

    def concluido(self):
        #self.gabarito_pessoal = list("acdeceeccadacdeceeccadcaacdeceddcacceddcacbacdeceeccadcacaacdeceddcacceddcacbacdeceeccadca")
        #self.gabarito_oficial = list("acdeceeccadacdeceeccadcaacdeceacdacceddcacbacdeceeccadcacaacdeceddcacceddcacbacdeceeccadca")
        pass

    def compactacao(self,lista_poluida):
        lista = str(lista_poluida).replace("', '","").replace("['","").replace("']","")
        return lista

    def ajeitarnumero(self,numero):
        if numero in range(1,10):
            return f"0{numero}"
        else: return numero

    def definir(self,emqualta):
        if emqualta == "pag3":
            return "pag4"
        else: return "pag3"


    def ta_marcado(self):
        time.sleep(.1)

        self.definircores()
        cor_marcado = self.cor4

        if self.gabarito_pessoal[self.indice_questao -1] == "a":
            self.cora =  cor_marcado
        if self.gabarito_pessoal[self.indice_questao -1] == "b":
            self.corb =  cor_marcado
        if self.gabarito_pessoal[self.indice_questao -1] == "c":
            self.corc =  cor_marcado
        if self.gabarito_pessoal[self.indice_questao -1] == "d":
            self.cord =  cor_marcado
        if self.gabarito_pessoal[self.indice_questao -1] == "e":
            self.core =  cor_marcado


    def colorir(self,letra):
        if letra[12:] == "a":
            return self.cora
        if letra[12:] == "b":
            return self.corb
        if letra[12:] == "c":
            return self.corc
        if letra[12:] == "d":
            return self.cord
        if letra[12:] == "e":
            return self.core
        else: return (1,0,0,1)



if __name__ == '__main__':
    GabarizandoApp().run()