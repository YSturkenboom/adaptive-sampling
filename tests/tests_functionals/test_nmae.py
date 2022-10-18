# coding=utf-8
# Copyright (c) DIRECT Contributors

import numpy as np
import pytest
import torch
from skimage.color import rgb2gray
from sklearn.datasets import load_sample_image

from direct.functionals.nmae import NMAELoss

# Load two images and convert them to grayscale
flower = rgb2gray(load_sample_image("flower.jpg"))[None].astype(np.float32)
china = rgb2gray(load_sample_image("china.jpg"))[None].astype(np.float32)


@pytest.mark.parametrize("image", [flower, china])
def test_nmae(image):
    image_batch = []
    image_noise_batch = []
    single_image_nmse = []

    for sigma in range(1, 5):
        noise = sigma * np.random.rand(*image.shape)
        image_noise = (image + noise).astype(np.float32).clip(0, 255)

        image_batch.append(image)
        image_noise_batch.append(image_noise)

    image_batch = np.stack(image_batch)
    image_noise_batch = np.stack(image_noise_batch)

    np_nmae = np.abs(image_batch - image_noise_batch).mean() / np.abs(image_batch).mean()

    image_batch_torch = torch.tensor(image_batch)
    image_noise_batch_torch = torch.tensor(image_noise_batch)

    nmse_batch = NMAELoss().forward(image_noise_batch_torch, image_batch_torch)
    assert np.allclose(nmse_batch, np_nmae, atol=5e-4)
