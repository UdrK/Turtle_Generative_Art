CHECKS_FOR_INTERSECTION = "checks_for_intersection"
CHECKS_FOR_INTERSECTION_DESCRIPTION = "Number intersection detections performed"

TOTAL_TIME_GETTING_NEARBY_POLYGONS = "total_time_getting_nearby_polygons"
TOTAL_TIME_GETTING_NEARBY_POLYGONS_DESCRIPTION = "Total time spent selecting nearby polygons for intersection detections"

DRAWING_TOTAL_TIME = "drawing_total_time"
DRAWING_TOTAL_TIME_DESCRIPTION = "Total drawing time"

POLYGONS_TRACED_NOT_DRAWN = "polygons_traced_not_drawn"
POLYGONS_TRACED_NOT_DRAWN_DESCRIPTION = "Number of polygons traced not drawn because an intersection was detected"

stat_ids = [DRAWING_TOTAL_TIME, POLYGONS_TRACED_NOT_DRAWN, CHECKS_FOR_INTERSECTION, TOTAL_TIME_GETTING_NEARBY_POLYGONS]
stat_descriptions = [DRAWING_TOTAL_TIME_DESCRIPTION, POLYGONS_TRACED_NOT_DRAWN_DESCRIPTION, CHECKS_FOR_INTERSECTION_DESCRIPTION, TOTAL_TIME_GETTING_NEARBY_POLYGONS_DESCRIPTION]