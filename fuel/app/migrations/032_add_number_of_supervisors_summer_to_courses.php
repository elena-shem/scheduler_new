<?php

namespace Fuel\Migrations;

class Add_number_of_supervisors_summer_to_courses
{
    public function up()
    {
        \DBUtil::add_fields('courses', array(
            'number_of_supervisors_summer' => array(
                'constraint' => 11, 
                'type'       => 'int',
                'null'       => false,
                'default'    => 0 
            ),
        ));
    }

    public function down()
    {
        \DBUtil::drop_fields('courses', array(
            'number_of_supervisors_summer'
        ));
    }
}