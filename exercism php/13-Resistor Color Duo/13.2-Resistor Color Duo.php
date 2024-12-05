<?php

declare(strict_types=1);

class ResistorColorDuo
{
    private $color_map = [
        "black" => "0",
        "brown" => "1",
        "red" => "2",
        "orange" => "3",
        "yellow" => "4",
        "green" => "5",
        "blue" => "6",
        "violet" => "7",
        "grey" => "8",
        "white" => "9"
    ];

    public function getColorsValue(array $colors): int
    {
        $total = "";
        for ($i = 0; $i < 2; $i++) {
            $total .= $this->color_map[$colors[$i]];
        }

        return (int) $total;
    }
}

?>