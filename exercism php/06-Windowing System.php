<?php

class ProgramWindow
{
    public $x;
    public $y;
    public $width;
    public $height;

    function __construct($x = 0, $y = 0, $width = 800, $height = 600) {
        $this->x = $x;
        $this->y = $y;
        $this->width = $width;
        $this->height = $height;
    }

    function resize($size) {
        $this->width = $size->width;
        $this->height = $size->height;
    }

    function move($position) {
        $this->x = $position->x;
        $this->y = $position->y;
    }
}

?>




<?php

class Size
{
    public $height;
    public $width;

    function __construct($height = 0, $width = 0) {
        $this->height = $height;
        $this->width = $width;
    }
}
?>



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