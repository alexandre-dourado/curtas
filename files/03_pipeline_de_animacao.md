# Pipeline Pragmático de Animação com IA (Passo a Passo)

Para contornar as limitações de consistência da IA de vídeo em formatos longos, utilizaremos a técnica de "Keyframe to Video".

## Fase 1: Preparação e Engenharia de Prompts (Local/CLI)
1.  **Organização:** Crie pastas para cada Cena (`/cena_01`, `/cena_02`, etc).
2.  **Contexto:** Mantenha o arquivo `04_guia_de_consistencia.md` alimentado no sistema (agente ou chat contínuo) para que a IA não "esqueça" o visual.

## Fase 2: Geração de Imagens (Keyframes)
Em vez de pedir o vídeo direto, gere o **primeiro quadro** de cada ação no gerador de imagens (Midjourney, DALL-E 3 ou Imagen 3 do próprio Gemini).
1.  Peça a imagem usando o *Guia de Consistência Visual*. Exemplo: *"Gere a imagem do Vilão (dreads) segurando o Azul pelo pescoço."*
2.  Se a imagem ficar boa, salve-a como `cena03_shot01_keyframe.jpg`.

## Fase 3: Geração de Vídeo (Image-to-Video)
1.  Use uma ferramenta de vídeo IA (Gen-3 Alpha da Runway, Luma Dream Machine, ou o gerador de vídeo embutido no seu pipeline).
2.  Faça o upload do `keyframe.jpg`.
3.  **Prompt de Movimento:** Descreva apenas a *física* e a *ação*, não descreva o cenário de novo. Exemplo: *"Faça uma animação stop-motion. O boneco com dreads levanta o braço rapidamente para dar um soco. A câmera treme levemente."*
4.  Gere clipes de 3 a 5 segundos no máximo.

## Fase 4: Pós-Produção (A Magia Real)
1.  Leve os clipes curtos gerados para um editor de vídeo (Premiere, CapCut).
2.  Costure os clipes seguindo o Roteiro (`02_roteiro_cena_a_cena.md`).
3.  **Crucial:** Adicione efeitos sonoros reais (Foley) de massinha batendo, arrastando, e a trilha de capoeira. É o som que "vende" a ilusão de peso e materialidade que a IA às vezes perde.
