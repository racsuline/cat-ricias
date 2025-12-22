import flet as ft

import flet_audio as fta

def main(page: ft.Page):
    page.title = "Cat-ricias"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 10
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    caricias = ft.Text("0")
    

    def contador(e):

        caricias.value = str(int(caricias.value) + 1)
        texto.value = f"Caricias: {caricias.value}"
        
        yupi.play()
        page.update()

    def sad_click(e):

        if e.state == ft.AudioState.PLAYING:
            meow_sad.pause()
        else:
            meow_sad.resume()
          
        page.update()

    max = ft.Container(
        content = ft.Image(src = "maxwell.png"),
        on_click = contador
    )
    
    texto = ft.Text(f"Caricias: {caricias.value}", size = 24)

    meow_sad = fta.Audio(
        src="meow_sad.mp3",
        autoplay=True
    )
    
    yupi = fta.Audio(
        src="yupi.mp3",
        on_state_changed = sad_click
    )
    

    page.overlay.append(meow_sad)
    page.overlay.append(yupi)

    page.add(
        ft.Text("Cat-ricias", size = 38, weight = "bold"),
        ft.Row(
            [
                texto
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        max
    )
    

ft.app(main)