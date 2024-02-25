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
Builder_string = ''' #:import c kivy.utils.get_color_from_hex
#: import CardTransition kivy.uix.screenmanager.CardTransition

WindowManager:
    #Resultados
    #Prova1
    Inicial
    Comecar
    Prova1
    Prova2
    Finalizar
    Resultados

<Inicial>
    name:"pag1"
    size:root.size
    FloatLayout:
        Image:
            source:"iniciar.png"
            pos_hint:{"center_x":0.5,"y":0.02}
            size_hint:None,None
            size:'62dp','62dp'
        Iniciarprova:
            size:self.size
            on_release:
                app.root.current = "pag2"
                root.manager.transition.direction = "up"
                root.manager.transition.duration = .4

        Button:
            pos_hint:{"center_x":0.16,"y":.02}
            size_hint:None,None
            #text:"Resuma"
            background_color: 0,0,0,0
            size:"62dp","62dp"
            on_release:
                app.resume()
                if app.pode_resumir == True: \
                app.root.current = "pag3"; \
                root.manager.transition.duration = .4
                root.manager.transition = CardTransition()
            canvas.before:
                Rectangle:
                    size:self.size
                    pos:self.pos
                    source:"resume.png"

        Button:
            pos_hint:{"center_x":0.84,"y":.02}
            size_hint:None,None
            #text:"Config"
            background_color: 0,0,0,0
            size:"62dp","62dp"
            on_release:
                #app.root.current = "pag3"
                #root.manager.transition.duration = .4
                #root.manager.transition = CardTransition()
            canvas.before:
                Rectangle:
                    size:self.size
                    pos:self.pos
                    source:"config.png"




        Titulo:

        Estatisticas:

<Iniciarprova@Button>
    text:""
    pos_hint:{"center_x":0.5,"y":0.04}
    size_hint:None,None
    size:'62dp','62dp'
    background_color: 0,0,0,0



# Superior
<Estatisticas@FloatLayout>
    size_hint:.85,.3
    pos_hint:{"center_x":0.5,"y":0.6}
    canvas.before:
        Color:
            rgba: app.cor5
        RoundedRectangle:
            size:self.size
            pos:self.pos

    Textodesempenho:
        text:"Desempenho:"
        font_size:"25dp"
        size:self.width,"30dp"
        padding_x:"0dp"
        pos_hint:{"x":0.01,"top":0.98}
    Textodesempenho:
        text:app.celula1
        pos_hint:{"x":0.01,"top":0.8}
    Textodesempenho:
        text:app.celula2
        pos_hint:{"x":0.01,"top":0.68}
    Textodesempenho:
        text:app.celula3
        pos_hint:{"x":0.01,"top":0.56}
    Textodesempenho:
        text:app.celula4
        pos_hint:{"x":0.01,"top":0.44}
    Textodesempenho:
        text:app.celula5
        pos_hint:{"x":0.01,"top":0.32}
    Textodesempenho:
        text:app.celula6
        pos_hint:{"x":0.01,"top":0.20}

<Textodesempenho@Label>
    #text:"Enem 1° dia  --  (50/90) "
    font_size:"18dp"
    size_hint:.9,None
    size:self.width,"20dp"
    pos_hint:{"x":.1,"top":.8}
    text_size:self.size
    halign:"left"
    valign:"top"
    color: app.cor6
    padding_x:"20dp"
    #canvas.before:
        #Color:
           # rgba: c("a4a4a4")
       # RoundedRectangle:
         #   size:self.size
          #  pos:self.pos




<Titulo>
    Label:
        size:root.width,root.height * .1
        text:root.texto()
        color:app.cor5
        font_size:"25dp"
        pos_hint:{"x":.1}
        top:root.height
        text_size:self.size
        halign:"left"
        valign:"top"
        padding:"15dp"
        #canvas.before:
            #Color:
                #rgba: c("a4a4a4")
            #RoundedRectangle:
                #size:self.size
                #pos:self.pos

# Inferior



<Comecar>
    name:"pag2"
    canvas.before:
        Color:
            rgba: app.cor2
        Rectangle:
            size:self.size
            pos:self.pos
    FloatLayout:
        Titulo2
        Back:
            padding:"5dp"
            x:"4dp"
            top:root.height*.98
        Entradadetexto:
            text:app.nome
            id: text_input
            cursor_color:app.cor7
        Submit:
            on_release:
                root.erro()
                if text_input.text != "": \
                app.extrairnome(text_input.text);\
                app.root.current = "pag3"
                #root.manager.transition.direction = "up"
               # app.sumario_geral()

<Entradadetexto>
    size_hint:.5,None
    multiline: False
    height:"30dp"
    pos_hint:{"center_x":.5,"y":.8}
    background_normal: ""
    background_color: 0,0,0,0
    canvas.before:
        Color:
            rgba: app.cor7
        Rectangle:
            pos:self.x,self.y
            size:self.width,2



<Back@Widget>
    size:'50dp','50dp'
    size_hint:None,None
    Image:
        source:"back.png"
        pos:root.pos
        size_hint:None,None
        size:root.size
    Button:
        text:""
        size_hint:None,None
        pos:root.pos
        size:root.size
        background_color: 0,0,0,0
        size:self.size
        on_release:
            app.root.current = "pag1"
           # root.manager.transition.direction = "up"

<Titulo2@Widget>
    Label:
        size:root.width,root.height * .1
        text:"Nomeie sua prova:"
        color:app.cor7
        font_size:"25dp"
        center_x:root.width*.5
        top:root.height*.98
        padding:"15dp"

<Submit>
    id:botao_submit
    text:"Concluído!"
    size_hint:.3,.05
    pos_hint:{"center_x":.5,"y":.7}
    background_normal: ""
    background_color: 0,0,0,0
    canvas.before:
        Color:
            rgba: app.cor7
        RoundedRectangle:
            pos:self.x,self.y
            size:self.size
            radius: [22]

<Textinhodeerro>
    size_hint:None,None
    #size:root.width *.5,"50dp"
    size:"100dp","50dp"
    text:"Preencha o nome da prova."
    color: app.cor5
    font_size:"13dp"
    padding:"15dp"


<Prova1>
    name:"pag3"
    canvas.before:
        Color:
            rgba: app.cor3
        Rectangle:
            pos:self.pos
            size:self.size
    FloatLayout:
        Label:
            id: nome_prova
            text:app.nome
            color:app.cor8
            size_hint:1,None
            height:"30dp"
            pos_hint:{"center_x":.5,"top":1}
            background_normal: ""
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: app.cor3
                Rectangle:
                    pos:self.x,self.y
                    size:self.size
        Sumario:
            id:sum_ario1
            size_hint: 1,None
            height:"120dp"
            pos_hint:{"center_x":.5}
            top:root.height - app.dpforpx(30)
            canvas.before:
                Color:
                    rgba: app.cor9
                Rectangle:
                    pos:self.pos
                    size:self.size

        Indice:
            text:app.texto_indice
            color:app.cor3
            font_size:"25dp"
            size_hint: .6,None
            height:"50dp"
            pos_hint:{"center_x":.5}
            top:root.height - app.dpforpx(158)
            canvas.before:
                Color:
                    rgba: app.cor4
                RoundedRectangle:
                    pos:self.pos
                    size:self.size
        Alternativas:
            size_hint: 1,None
            height:"520dp"
            pos_hint:{"center_x":.5}
            top:root.height - app.dpforpx(200)
            orientation:"vertical"
            spacing:"28dp"
            padding:"28dp"
            Alternativa:
                text:"Alternativa a"
                canvas.before:
                    Color:
                        rgba: app.cora
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[28]
                on_release:
                    app.assinalar("a")
                    app.ta_marcado()
            Alternativa:
                text:"Alternativa b"
                canvas.before:
                    Color:
                        rgba: app.corb
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[28]
                on_release:
                    app.assinalar("b")
                    app.ta_marcado()
            Alternativa:
                text:"Alternativa c"
                canvas.before:
                    Color:
                        rgba: app.corc
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[28]
                on_release:
                    app.assinalar("c")
                    app.ta_marcado()
            Alternativa:
                text:"Alternativa d"
                canvas.before:
                    Color:
                        rgba: app.cord
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[28]
                on_release:
                    app.assinalar("d")
                    app.ta_marcado()
            Alternativa:
                text:"Alternativa e"
                canvas.before:
                    Color:
                        rgba: app.core
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[28]
                on_release:
                    app.assinalar("e")
                    app.ta_marcado()

        Rodape:
            size_hint: 1,None
            height:"80dp"
            pos_hint:{"center_x":.5,"y":0}
            canvas.before:
                Color:
                    rgba: app.cor9
                Rectangle:
                    pos:self.pos
                    size:self.size
            Button:
                text:"Concluído"
                size_hint:None,None
                size:root.width*.28,"50dp"
                y:"10dp"
                center_x:root.width*.5
                color:app.cor3
                text_size:self.size
                halign:"center"
                valign:"center"
                padding_x:"10dp"
                background_color:0,0,0,0
                on_release:
                    app.gab_oficial_entrada = 0
                    app.atualizar()
                    app.concluido()
                    app.root.current = "pag5"
                    root.manager.transition.direction = "up"
                    #root.manager.transition = CardTransition()
                    root.manager.transition.duration = .1
                canvas.before:
                    Color:
                        rgba: app.cor5
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[12]
            Button:
                text:"<"
                size_hint:None,None
                size:root.width*.28,"50dp"
                y:"10dp"
                center_x:root.width*.17
                color:app.cor3
                font_size:"30dp"
                text_size:self.size
                halign:"center"
                valign:"center"
                padding_x:"10dp"
                background_color:0,0,0,0
                on_release:
                    app.atualizar()
                    if app.indice_questao != 1: \
                    app.voltar(); \
                    app.root.current = "pag4"
                    root.manager.transition.direction = "right"
                    #root.manager.transition = CardTransition()
                    root.manager.transition.duration = .1
                    app.ta_marcado()
                canvas.before:
                    Color:
                        rgba:app.cor5
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[12]
            Button:
                text:">"
                size_hint:None,None
                size:root.width*.28,"50dp"
                y:"10dp"
                center_x:root.width*.83
                color:app.cor3
                font_size:"30dp"
                text_size:self.size
                halign:"center"
                valign:"center"
                padding_x:"10dp"
                background_color:0,0,0,0
                on_release:
                    app.atualizar()
                    root.manager.transition.direction = "left"
                    root.manager.transition = CardTransition()
                    root.manager.transition.duration = .1

                    app.avancar()
                    app.root.current = "pag4"

                    app.ta_marcado()
                canvas.before:
                    Color:
                        rgba: app.cor5
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[12]

<Prova2>
    name:"pag4"
    canvas.before:
        Color:
            rgba: app.cor3
        Rectangle:
            pos:self.pos
            size:self.size
    FloatLayout:
        Label:
            id: nome_prova
            text:app.nome
            color:app.cor8
            size_hint:1,None
            height:"30dp"
            pos_hint:{"center_x":.5,"top":1}
            background_normal: ""
            background_color: 0,0,0,0
            canvas.before:
                Color:
                    rgba: app.cor3
                Rectangle:
                    pos:self.x,self.y
                    size:self.size
        Sumario:
            id: sum_ario2
            size_hint: 1,None
            height:"120dp"
            pos_hint:{"center_x":.5}
            top:root.height - app.dpforpx(30)
            orientation:"lr-tb"
            canvas.before:
                Color:
                    rgba: app.cor9
                Rectangle:
                    pos:self.pos
                    size:self.size



        Indice:
            text:app.texto_indice
            color:app.cor3
            font_size:"25dp"
            size_hint: .6,None
            height:"50dp"
            pos_hint:{"center_x":.5}
            top:root.height - app.dpforpx(158)
            canvas.before:
                Color:
                    rgba: app.cor4
                RoundedRectangle:
                    pos:self.pos
                    size:self.size
        Alternativas:
            size_hint: 1,None
            height:"520dp"
            pos_hint:{"center_x":.5}
            top:root.height - app.dpforpx(200)
            orientation:"vertical"
            spacing:"28dp"
            padding:"28dp"
            Alternativa:
                text:"Alternativa a"
                canvas.before:
                    Color:
                        rgba: app.cora
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[28]
                on_release:
                    app.assinalar("a")
                    app.ta_marcado()
            Alternativa:
                text:"Alternativa b"
                canvas.before:
                    Color:
                        rgba: app.corb
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[28]
                on_release:
                    app.assinalar("b")
                    app.ta_marcado()
            Alternativa:
                text:"Alternativa c"
                canvas.before:
                    Color:
                        rgba: app.corc
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[28]
                on_release:
                    app.assinalar("c")
                    app.ta_marcado()
            Alternativa:
                text:"Alternativa d"
                canvas.before:
                    Color:
                        rgba: app.cord
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[28]
                on_release:
                    app.assinalar("d")
                    app.ta_marcado()
            Alternativa:
                text:"Alternativa e"
                canvas.before:
                    Color:
                        rgba: app.core
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[28]
                on_release:
                    app.assinalar("e")
                    app.ta_marcado()

        Rodape:
            size_hint: 1,None
            height:"80dp"
            pos_hint:{"center_x":.5,"y":0}
            canvas.before:
                Color:
                    rgba: app.cor9
                Rectangle:
                    pos:self.pos
                    size:self.size
            Button:
                text:"Concluído"
                size_hint:None,None
                size:root.width*.28,"50dp"
                y:"10dp"
                center_x:root.width*.5
                color:app.cor3
                font_size:"15dp"
                text_size:self.size
                halign:"center"
                valign:"center"
                padding_x:"10dp"
                background_color:0,0,0,0
                on_release:
                    app.atualizar()
                    app.gab_oficial_entrada = 0
                    app.root.current = "pag5"
                    root.manager.transition.direction = "up"
                    #root.manager.transition = CardTransition()
                    root.manager.transition.duration = .1
                canvas.before:
                    Color:
                        rgba: app.cor5
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[12]
            Button:
                text:"<"
                size_hint:None,None
                size:root.width*.28,"50dp"
                y:"10dp"
                center_x:root.width*.17
                color:app.cor3
                font_size:"30dp"
                text_size:self.size
                halign:"center"
                valign:"center"
                padding_x:"10dp"
                background_color:0,0,0,0
                on_release:
                    if app.indice_questao != 1: \
                    app.voltar(); \
                    app.atualizar()
                    app.root.current = "pag3"
                    root.manager.transition.direction = "right"
                    #root.manager.transition = CardTransition()
                    root.manager.transition.duration = .1
                    app.ta_marcado()
                canvas.before:
                    Color:
                        rgba: app.cor5
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[12]
            Button:
                text:">"
                size_hint:None,None
                size:root.width*.28,"50dp"
                y:"10dp"
                center_x:root.width*.83
                color:app.cor3
                font_size:"30dp"
                text_size:self.size
                halign:"center"
                valign:"center"
                padding_x:"10dp"
                background_color:0,0,0,0
                on_release:
                    app.atualizar()
                    app.avancar()
                    app.root.current = "pag3"
                    root.manager.transition.direction = "left"
                    #root.manager.transition = CardTransition()
                    root.manager.transition.duration = .1
                    app.ta_marcado()
                canvas.before:
                    Color:
                        rgba: app.cor5
                    RoundedRectangle:
                        pos:self.pos
                        size:self.size
                        radius:[12]



<Sumario>
    #ordem left,top,right,bottom
   # padding:"10dp","2dp","10dp","2dp"
    #spacing:"1dp"


<Botao_do_sumario>
    size_hint:.0545,None
    height:"22dp"
    color: app.cor4
    font_size:"13dp"
    halign:"center"
    valign:"center"
    text_size:self.size
    background_color:0,0,0,0
    on_release:
        app.ir(self.text)
        app.root.current = app.definir(app.root.current)




<Indice@Label>

<Rodape@Widget>

<Alternativas@BoxLayout>
   # canvas.before:
        #Color:
         #   rgba: c("#ccfff7")
        #Rectangle:
         #   pos:self.pos
         # size:self.size

<Alternativa>
    color:app.cor3
    font_size:"20dp"
    text_size:self.size
    halign:"left"
    valign:"center"
    padding_x:"10dp"
    background_color:0,0,0,0
    on_release:
        app.ta_marcado()



<Finalizar@Screen>
    name:"pag5"
    canvas.before:
        Color:
            rgba: app.cor1
        Rectangle:
            pos:self.pos
            size:self.size
    FloatLayout:
        Label:
            size_hint:1,.1
            pos_hint:{"center_x":.5,"top":.98}
            text:"Gabarito oficial:"
            color:app.cor5
            font_size:"25dp"
            padding:"15dp"
        Entradadetexto:
            text:app.gab_oficial_entrada
            id:entrada_gab
        Label:
            size_hint:None,None
            size:root.width *.5,"50dp"
            pos_hint:{"center_x":.5,"top":.78}
            text:"Exemplo: abcdadedabacdaeeda.\nsem espaços entre as respostas.\nse houver alguma anulada ponha X\nno gabarito.\nnão insira numeros."
            color: app.cor10
            font_size:"11dp"
            padding:"15dp"
        Label:
            size_hint:None,None
            size: "40dp","40dp"
            pos_hint:{"center_x":.85,"y":.8}
            text:app.tamanho(entrada_gab.text)
            color:app.cor5
            font_size:"18dp"
            padding:"15dp"
            canvas.before:
                Color:
                    rgba: app.cor10
                Rectangle:
                    pos:self.pos
                    size:self.size
        Button:
            id:botao_submit1
            text:"Concluído!"
            size_hint:.3,.05
            pos_hint:{"center_x":.5,"y":.63}
            background_normal: ""
            background_color: 0,0,0,0
            on_release:
                app.root.current = "pag6"
                app.correcao()
                app.salvar_como_concluido()
            canvas.before:
                Color:
                    rgba: app.cor7
                RoundedRectangle:
                    pos:self.x,self.y
                    size:self.size
                    radius: [22]





<Resultados@Screen>
    name: "pag6"
    canvas.before:
        Color:
            rgba: app.cor1
        Rectangle:
            pos:self.pos
            size:self.size
    FloatLayout:
        Label:
            size_hint:1,.05
            pos_hint:{"center_x":.5,"top":1}
            text:"Resultados:"
            color:app.cor5
            font_size:"25dp"
            padding:"15dp"
        Label:
            size_hint:1,.1
            pos_hint:{"center_x":.25,"top":.97}
            text:"Questões incorretas:"
            color:app.cor5
            font_size:"18dp"
            padding:"15dp"
        Label:
            text: app.gabarito_incorreto_formatado
            size_hint:.5,1
            pos_hint:{"center_x":.25,"top":.92}
            color:app.cor5
            font_size:"15dp"
            padding:"15dp"
            halign:"left"
            valign:"top"
            text_size:self.size
            #canvas.before:
                #Color:
                    #rgba: c("#FFFFFF")
                #Rectangle:
                    #pos:self.pos
                    #size:self.size
        Label:
            size_hint:1,.1
            pos_hint:{"center_x":.75,"top":.97}
            text:"Numeros de acertos:"
            color:app.cor5
            font_size:"18dp"
            padding:"15dp"
        Label:
            size_hint:1,.1
            pos_hint:{"center_x":.75,"top":.94}
            text:app.numero_de_acertos_formatado
            color:app.cor5
            font_size:"18dp"
            padding:"15dp"
        Label:
            size_hint:1,.1
            pos_hint:{"center_x":.75,"top":.84}
            text:"nome da prova:"
            color:app.cor5
            font_size:"18dp"
            padding:"15dp"
        Label:
            size_hint:1,.1
            pos_hint:{"center_x":.75,"top":.81}
            text:app.nome
            color:app.cor5
            font_size:"14dp"
            padding:"15dp"
        Button
            id:botao_submit2
            text:"Finalizar"
            size_hint:.3,.05
            pos_hint:{"center_x":.5,"y":.1}
            background_normal: ""
            background_color: 0,0,0,0
            on_release:
                app.root.current = "pag1"
                app.resetar()
            canvas.before:
                Color:
                    rgba: app.cor7
                RoundedRectangle:
                    pos:self.x,self.y
                    size:self.size
                    radius: [22]
        Button
            id:botao_submit2
            text:"Editar gabarito"
            size_hint:.3,.05
            pos_hint:{"center_x":.5,"y":.19}
            background_normal: ""
            background_color: 0,0,0,0
            on_release:
                app.root.current = "pag5"
            canvas.before:
                Color:
                    rgba: app.cor7
                RoundedRectangle:
                    pos:self.x,self.y
                    size:self.size
                    radius: [22]   '''
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
       return Builder.load_string(Builder_string)


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