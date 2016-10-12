season_colors = (sns.color_palette("BuPu", 3) +
                 sns.color_palette("RdPu", 3) +
                 sns.color_palette("YlGn", 3) +
                 sns.color_palette("OrRd", 3))
g = sns.clustermap(flights, row_colors=season_colors)
