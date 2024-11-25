<?php

class ProgramWindow
{
   public $x;
   public $y;
   public $height;
   public $width;

    function __construct() {
        $this->x = 0;
        $this->y = 0;
        $this->width = 800;
        $this->height = 600;
    }

    function resize(Size $size) {
        $this->width = $size->width;
        $this->height = $size->height;
    }

    function move(Position $position) {
        $this->x = $position->x;
        $this->y = $position->y;
    }
}





<?php

class Size 
{
    function __construct($height, $width) {
        $this->height = $height;
        $this->width = $width;
    } 
}




<?php

class Position
{
    public $x;
    public $y;

    function __construct($y = 0, $x = 0) {
        $this->x = $x;
        $this->y = $y;
    }
}
?>