from ide.building_blocks.dependency_measure import dCor
from ide.building_blocks.dependency_test_adapter import DependencyTestAdapter
from ide.core.blueprint_factory import BlueprintFactory
from ide.modules.oracle.data_source import IndependentDataSetDataSource, LineDataSource, SquareDataSource
from ide.modules.oracle.data_source_adapter import DataSourceAdapter
from distribution_data_generation.data_sources.double_linear_data_source import DoubleLinearDataSource
from distribution_data_generation.data_sources.hourglass_data_source import HourglassDataSource
from distribution_data_generation.data_sources.hypercube_data_source import HypercubeDataSource
from distribution_data_generation.data_sources.graph_data_source import GraphDataSource
from distribution_data_generation.data_sources.sine_data_source import SineDataSource
from distribution_data_generation.data_sources.star_data_source import StarDataSource
from distribution_data_generation.data_sources.z_data_source import ZDataSource
from distribution_data_generation.data_sources.inv_z_data_source import InvZDataSource
from distribution_data_generation.data_sources.cross_data_source import CrossDataSource

test = DependencyTestAdapter(
                dependency_measure=dCor(),
        )

blueprints = BlueprintFactory.getBlueprintsForSyntheticData(algorithms=[test], dataSources=[IndependentDataSetDataSource(number_of_distributions=10, dims = 4)])