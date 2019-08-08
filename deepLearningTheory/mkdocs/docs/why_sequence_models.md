# Why sequence models

Models like recurrent neural networks or RNNs have transformed:

- speech recognition
- music generation
- natural language processing and other areas

Examples:

| Type                    | Input X | Output Y |
|-------------------------|---------|----------|
| Speech recognition      | ![speech](img/speech_sound.png) | The quick brown fox jumped ofver the lazy dog. |
| Music generation      | Empty set, or it can be a single integer, maybe referring to the genre of music you want to generate or maybe the first few notes of the piece of music you want.        | ![music](img/music.png) |
| Sentiment classification      | "There is nothing to like in this movie" | ![stars](img/stars.png) |
| DNA analysis      | AGCCCCTGTGAGGAACTAG | ![stars](img/dna.png) |
| Machine translation | "Voulez-vous chanter avec moi?" | "Do you want to sing with me?" |
| Video activity recognition | ![Runnning](img/running.png) | Running |
| Name entity recognition | Yesterday Harry Potter met Hermione Granger. | Yesterday **Harry Potter** met **Hermione Granger**. |

In the case of detecting a name: The RNN should predict if the next word is a name based on previous experiences of seeing sequences of words.