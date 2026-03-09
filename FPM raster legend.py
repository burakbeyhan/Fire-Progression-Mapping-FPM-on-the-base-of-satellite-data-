"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""
# import qgis.utils
import numpy as npy
from matplotlib import colormaps
from PyQt5.QtGui import QColor
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       # QgsProcessingParameterRasterDestination,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterRasterLayer,
                       QgsRasterBandStats, 
                       QgsGradientStop, 
                       QgsGradientColorRamp, 
                       QgsSingleBandPseudoColorRenderer,
                       QgsStyle)

class FPMRasterLegend(QgsProcessingAlgorithm):
    """
    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    INPUT = 'INPUT'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return FPMRasterLegend()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'FPM_Raster_Legend'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('FPM Raster Legend')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('FPM')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'FPMrasterlegend'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("Apply spectrum color-ramp for fire isochrone map")

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """
        # We add the input vector features source. It can have any kind of
        # geometry.

        self.addParameter(
            QgsProcessingParameterRasterLayer(
                self.INPUT,
                self.tr('Input Raster layer'),
                [QgsProcessing.TypeRaster]
            )
        )
        
    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """
        # Retrieve the feature source and sink. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        layer = self.parameterAsRasterLayer(
            parameters,
            'INPUT',
            context)
            
        # define color map by name
        cmap = colormaps['Spectral']

        # get min/max values
        minmax = layer.dataProvider().bandStatistics(1, QgsRasterBandStats.All)
        valmin = minmax.minimumValue
        valmax = minmax.maximumValue

        # limit number of color steps to 30
        if cmap.N > 30:
            colors = cmap(npy.linspace(1, cmap.N, 30, dtype=npy.int16))
        else:
            colors = cmap(range(1,cmap.N))
        colorsN = len(colors)

        # making a colorRamp-list
        colorsList = []
        for idx, col in enumerate(colors):
            qcol = QColor(int(col[0]*255), int(col[1]*255), int(col[2]*255))
            if idx == 0:
                startColor = qcol
            elif idx == colorsN - 1:
                endColor = qcol
            else:
                val = idx * 1/colorsN
                colorsList.append( QgsGradientStop((idx + 1) * 1 / (colorsN - 1), qcol) )
        
        colorRamp = QgsGradientColorRamp(startColor, endColor, False, colorsList)

        renderer = QgsSingleBandPseudoColorRenderer(layer.dataProvider(), 1)
        renderer.setClassificationMin(valmin)
        renderer.setClassificationMax(valmax)
        renderer.createShader(colorRamp)
       
        layer.setRenderer(renderer)
        layer.triggerRepaint()
        
        return {}