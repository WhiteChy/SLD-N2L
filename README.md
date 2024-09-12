# DEMO
[https://whitechy.github.io/SLD-N2L/](https://whitechy.github.io/SLD-N2L/)

Due to corporation, I can't upload the code.

You can refer [Freevc](https://github.com/OlaWod/FreeVC) and [VITS-VC](https://github.com/jaywalnut310/vits) to replicate this work.

The dataset is [EMALG](https://github.com/ASP-WHU/EMALG). The speaker ID in test set is F137 F207 M129 M132.

The metric ASR, UTMOS, F0CORR, subjective MOS can be found at [PitchVC](https://github.com/OlaWod/PitchVC).


Baselines are replicated by replacing the speaker embedding with Lombard embedding.

[StarGAN](https://github.com/thestarboy/StarGAN-Voice-Conversion-2)

[CycleGAN](https://github.com/shreyas253/CycleGAN_1dCNN) (PML vocoder & model from official code show poor quality. I replicate CycleGAN using this version(https://github.com/leimao/Voice-Converter-CycleGAN))

[Freevc](https://github.com/OlaWod/FreeVC)

[DDDMVC](https://github.com/hayeong0/DDDM-VC)) (The poor quality may be due to the non-fine-tuned hubert and non-fine-tuned HifiGAN)

Thanks to [OlaWod](https://github.com/OlaWod)!!!!!!
