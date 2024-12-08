<?php

declare(strict_types=1);

function toRna(string $dna): string
{
    $dnaToRna = ["G" => "C", "C" => "G", "T" => "A", "A" => "U"];
    $rna = '';
    $dnaUpper = strtoupper($dna);

    for ($i = 0; $i < strlen($dnaUpper); $i++) {
        $rna .= $dnaToRna[$dnaUpper[$i]];
    }

    return $rna;
}

?>