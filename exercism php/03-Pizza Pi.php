<?php

class PizzaPi
{
    public function calculateDoughRequirement($numberOfPizzas, $servingsPerPizza)
    {
        $doughPerPizza = ($servingsPerPizza * 20) + 200;
        return round($numberOfPizzas * $doughPerPizza);
    }

    public function calculateSauceRequirement($pizza, $can)
    {
        return $pizza * 125 / $can;
    }

    public function calculateCheeseCubeCoverage($cheese_dimension, $thickness, $diameter)
    {
        $cheese_volume = $cheese_dimension * $cheese_dimension * $cheese_dimension;
        $cheese_per_pizza = $thickness * pi() * $diameter;
        return floor($cheese_volume / $cheese_per_pizza);
    }

    public function calculateLeftOverSlices($pizza, $friends)
    {
        return ($pizza * 8) % $friends;
    }
}