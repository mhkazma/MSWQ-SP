# MSWQ-SP

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24544993.svg)](https://doi.org/10.5281/zenodo.24544993)

**Results and plotting scripts for:**

> **Observability and Generalized Sensor Placement for Nonlinear Quality Models in Drinking Water Networks**
>
> M. H. Kazma, S. M. Elsherif, and A. F. Taha
>
> *Journal of Water Process Engineering*, 77, 108339 (2025). Published 8 August 2025. https://doi.org/10.1016/j.jwpe.2025.108339 (arXiv: https://arxiv.org/abs/2411.04202)

Water quality sensor placement in drinking water networks usually relies on single-species chlorine decay models and on a single hydraulic profile. This paper instead quantifies the observability of nonlinear multi-species chlorine transport, decay, and reaction dynamics with a moving horizon formulation, and uses observability measures (log determinant and trace) that keep the submodular structure of the sensor selection problem. A greedy algorithm then gives one sensor configuration that is robust to varying demand patterns and water quality conditions. The repository contains the observability measures and optimal sensor configurations computed for EPANET Net1 and Net2 under three hydraulic profiles, and for Net1 also under two changes of the multi-species reaction coefficient and initial conditions, and the scripts that plot the figures of the paper.

## Contents

| Folder | Content |
|---|---|
| `NET1/` | Observability measures and sensor configurations for EPANET Net1 (hydraulic profiles CS1 to CS3, multi-species models MSX1 to MSX3) |
| `NET2/` | Observability measures and sensor configurations for EPANET Net2 (hydraulic profiles CS1 to CS3) |
| `Plots/` | Scripts that plot the results of the paper from the `.mat` files |

## Requirements

- Python 3 with numpy, scipy, matplotlib, seaborn, and pandas
- MATLAB, for `PlotTime.m` and the demand pattern plots

## Citation

```bibtex
@article{kazma2025observability,
  title   = {Observability and generalized sensor placement for nonlinear quality models
             in drinking water networks},
  author  = {Kazma, Mohamad H. and Elsherif, Salma M. and Taha, Ahmad F.},
  journal = {Journal of Water Process Engineering},
  volume  = {77},
  pages   = {108339},
  year    = {2025},
  doi     = {10.1016/j.jwpe.2025.108339},
  note    = {Published 8 August 2025. arXiv:2411.04202}
}
```

To cite the results and scripts themselves (version 1.0, archived on Zenodo):

```bibtex
@misc{kazma2025mswqsp,
  author       = {Kazma, Mohamad H. and Elsherif, Salma M. and Taha, Ahmad F.},
  title        = {{MSWQ-SP}: Observability and generalized sensor placement for nonlinear water quality
                  models (results and plotting scripts, Version 1.0)},
  howpublished = {Zenodo},
  year         = {2026},
  doi          = {10.5281/zenodo.24544993}
}
```

## License

MIT, see [LICENSE](LICENSE).
