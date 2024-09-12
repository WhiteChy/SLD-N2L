# DEMO
[https://whitechy.github.io/SLD-N2L/](https://whitechy.github.io/SLD-N2L/)

Due to corporation, I can't upload the code.

---------------------------------------------------------------------------------------------------------------------------------
# some details

You can refer [Freevc](https://github.com/OlaWod/FreeVC), [VITS-VC](https://github.com/jaywalnut310/vits) and the paper to replicate this work.

The dataset is [EMALG](https://github.com/ASP-WHU/EMALG). The speaker ID in test set is F137 F207 M129 M132.
The metric ASR, UTMOS, subjective MOS can be found at [PitchVC](https://github.com/OlaWod/PitchVC).

Baselines are replicated by replacing the speaker embedding with Lombard embedding.

[StarGAN](https://github.com/thestarboy/StarGAN-Voice-Conversion-2) (model architecture and hyperparameters are built based on [Speech_Intelligibility_Enhancement_Using_Non-Parallel_Speaking_Style_Conversion_With_Stargan_And_Dynamic_Range_Compression](https://ieeexplore.ieee.org/abstract/document/9102916/))

[CycleGAN](https://github.com/shreyas253/CycleGAN_1dCNN) (PML vocoder & model from official code show poor quality. I replicate CycleGAN using this version(https://github.com/leimao/Voice-Converter-CycleGAN))

[Freevc](https://github.com/OlaWod/FreeVC)

[DDDMVC](https://github.com/hayeong0/DDDM-VC)) (The poor quality may be due to the non-fine-tuned hubert and non-fine-tuned HifiGAN)

Thanks to [OlaWod](https://github.com/OlaWod)!!!!!!!!!

The software of subjective intelligibility test: 

![intelligibility](data/intelligibility.png)
