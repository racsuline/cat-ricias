import flet as ft

import flet_audio as fta

def main(page: ft.Page):
    page.title = "Cat-ricias"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 10
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    caricias = ft.Text("99")
    max_image = ft.Image(src="maxwell.png", height = 400, width = 400)
    

    def contador(e):

        caricias.value = str(int(caricias.value or "0") + 1)
        texto.value = f"Acaricia al pobre gato_meme.png | Caricias: {caricias.value}"

        # Cada 100 clicks: reemplazar temporalmente la imagen por el gif y reproducir audio especial
        if int(caricias.value) % 100 == 0:
            max_image.src = "maxspin.gif"  # usa la ruta que ya configuraste
            page.update()
            dance.play()
        else:
            yupi.play()
            page.update()

    def sad_click(e):
        # Pausar/resumir el fondo cuando suena el click normal
        if e.state == fta.AudioState.PLAYING:
            meow_sad.pause()
        elif e.state in (fta.AudioState.PAUSED, fta.AudioState.STOPPED, fta.AudioState.COMPLETED):
            meow_sad.resume()
        page.update()

    def dance_state_changed(e):
        # Pausar fondo durante audio especial y restaurar imagen al terminar
        if e.state == fta.AudioState.PLAYING:
            meow_sad.pause()
        elif e.state in (fta.AudioState.COMPLETED, fta.AudioState.STOPPED):
            max_image.src = "maxwell.png"
            page.update()
            meow_sad.resume()

    max = ft.Container(content=max_image, on_click=contador)
    
    texto = ft.Text(f"Acaricia al pobre gato_meme.png | Caricias: {caricias.value}", size = 24)

    meow_sad = fta.Audio(
        src="meow_sad.mp3",
        autoplay=True
    )
    
    yupi = fta.Audio(
        src="yupi.mp3",
        on_state_changed = sad_click
    )
    
    # Audio especial de celebración cada 100 clicks
    dance = fta.Audio(
        src="dance.mp3",
        on_state_changed=dance_state_changed
    )
    

    page.overlay.append(meow_sad)
    page.overlay.append(yupi)
    page.overlay.append(dance)

    page.add(
        ft.Text("Cat-ricias", size = 38, weight = ft.FontWeight.BOLD),
        ft.Row(
            [
                texto
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        max
    )
    

ft.app(main)