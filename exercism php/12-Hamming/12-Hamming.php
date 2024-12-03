<?php

declare(strict_types=1);

function distance(string $strandA, string $strandB): int
{
    if (strlen($strandA) !== strlen($strandB)) {
        throw new InvalidArgumentException('strands must be of equal length');
    }

    $hamming = 0;

    for ($i = 0; $i < strlen($strandA); $i++) {
        if ($strandA[$i] !== $strandB[$i]) {
            $hamming++;
        }
    }

    return $hamming;
}