import cv2 as cv
import os
from ImageHandler import ImageHandler

# The files and directories to be used.
plate3 = 'entry-3/picasso_bull_plate_3_no_ground.tif'
plate3_1 = 'entry-3/picasso_bull_plate_3_half_cut.tif'
plate3_2 = 'entry-3/picasso_bull_plate_3_more_cut.tif'
plate3_3 = 'entry-3/picasso_bull_plate_3_front_cut.tif'
plate3_4 = 'entry-3/picasso_bull_plate_3_new_head.tif'
plate4 = 'entry-3/picasso_bull_plate_4_no_ground.tif'

step_log = 'entry-3'

bull3 = ImageHandler(plate3, step_log)
bull4 = ImageHandler(plate4, step_log)
bull3_1 = ImageHandler(plate3_1, step_log)
bull3_2 = ImageHandler(plate3_2, step_log)
bull3_3 = ImageHandler(plate3_3, step_log)
bull3_4 = ImageHandler(plate3_4, step_log)

bull3.draw_middle_line()
bull3.draw_center_of_mass()
bull3.save_color('./jpg/picasso_bull_plate_3_com.jpg')

bull4.draw_middle_line()
bull4.draw_center_of_mass()
bull4.save_color('./jpg/picasso_bull_plate_4_com.jpg')

bull3_1.draw_middle_line()
bull3_1.draw_center_of_mass()
bull3_1.save_color('./jpg/picasso_bull_plate_3_com_half_cut.jpg')

bull3_2.draw_middle_line()
bull3_2.draw_center_of_mass()
bull3_2.save_color('./jpg/picasso_bull_plate_3_com_more_cut.jpg')

bull3_3.draw_middle_line()
bull3_3.draw_center_of_mass()
bull3_3.save_color('./jpg/picasso_bull_plate_3_com_front_cut.jpg')

bull3_4.draw_middle_line()
bull3_4.draw_center_of_mass()
bull3_4.save_color('./jpg/picasso_bull_plate_3_com_new_head.jpg')

# bull3.show_color('Bull3')
# bull4.show_color('Bull4')
# bull3_1.show_color('Bull3.1')
# bull3_2.show_color('Bull3.2')
# bull3_3.show_color('Bull3.3')
# bull3_4.show_color('Bull3.4')