<?php

declare(strict_types=1);

class Tournament
{
    private $teams = [];

    public function tally(string $scores): string
    {
        if (empty($scores)) {
            return "Team                           | MP |  W |  D |  L |  P";
        }

        $matches = explode("\n", $scores);
        
        foreach ($matches as $match) {
            if (empty($match)) {
                continue;
            }

            $parts = explode(";", $match);
            
            if (count($parts) != 3) {
                continue;
            }
            
            $team1 = trim($parts[0]);
            $team2 = trim($parts[1]);
            $result = trim($parts[2]);

            $this->addMatch($team1, $team2, $result);
        }

        $this->getSortedTeams();
        
        $output = $this->generateTable($scores);
        if (!empty($output)) {
        $output = rtrim($output, "\n");
    }

    return $output;
    }

    private function addMatch(string $team1, string $team2, string $result)
    {
        if (!isset($this->teams[$team1])) {
            $this->teams[$team1] = new Team($team1);
        }
        if (!isset($this->teams[$team2])) {
            $this->teams[$team2] = new Team($team2);
        }

        $this->teams[$team1]->updateStats($result, $this->teams[$team1]);
        $this->teams[$team2]->updateStats($result === "win" ? "loss" : ($result === "loss" ? "win" : "draw"), $this->teams[$team2]);
    }

    private function getSortedTeams()
    {
        usort($this->teams, function($a, $b) {
            if ($a->points === $b->points) {
                return strcmp($a->name, $b->name);
            }
            return $b->points - $a->points;
        });
    }

    private function generateTable(): string
    {
        $table = "Team                           | MP |  W |  D |  L |  P\n";
        foreach ($this->teams as $team) {
            $table .= $team->getStats() . "\n";
        }
        return $table;
    }
}

class Team
{
    public $name;
    public $matches = 0;
    public $win = 0;
    public $draw = 0;
    public $loss = 0;
    public $points = 0;

    public function __construct($name)
    {
        $this->name = $name;
    }

    public function updateStats($result, Team $opponent)
    {
        $this->matches++;

        switch ($result) {
            case "win":
                $this->win++;
                $this->points += 3;
                break;
            case "draw":
                $this->draw++;
                $this->points += 1;
                break;
            case "loss":
                $this->loss++;
                break;
        }
    }

    public function getStats()
    {
        return sprintf("%-30s | %2d | %2d | %2d | %2d | %2d", 
                        $this->name, $this->matches, $this->win, 
                        $this->draw, $this->loss, $this->points);
    }
}
?>