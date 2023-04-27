from django.core.management.base import BaseCommand
from projects.models import UNGoals, EngDiscipline

class Command(BaseCommand):
    help = 'Create the default discipline and UN SDG field entries for projects'

    def handle(self, *args, **kwargs):
        disciplines = ["Computer", "Software", "Electrical", "Civil", "Mechanical", "Space", "Geomatics", "Other"]
        disc_obj = [EngDiscipline(discipline=d) for d in disciplines]
        EngDiscipline.objects.bulk_create(disc_obj)

        '''id = models.IntegerField(primary_key = True)
            title = models.CharField(max_length = 50)
            description = models.TextField()
            link = models.TextField()'''
        sdgs = []
        sdgs.append(UNGoals(id=1, title='No Poverty', description='End poverty in all its forms everywhere', link='https://sdgs.un.org/goals/goal1'))
        sdgs.append(UNGoals(id=2, title='Zero Hunger', description='End hunger, achieve food security and improve nutrition and promote sustainable agriculture', link='https://sdgs.un.org/goals/goal2'))
        sdgs.append(UNGoals(id=3, title='Good Health and Well-Being', description='Ensure healthy lives and promote well-being for all at all ages', link='https://sdgs.un.org/goals/goal3'))
        sdgs.append(UNGoals(id=4, title='Quality Education', description='Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all', link='https://sdgs.un.org/goals/goal4'))
        sdgs.append(UNGoals(id=5, title='Gender Equality', description='Achieve gender equality and empower all women and girls', link='https://sdgs.un.org/goals/goal5'))
        sdgs.append(UNGoals(id=6, title='Clean Water and Sanitation', description='Ensure availability and sustainable management of water and sanitation for all', link='https://sdgs.un.org/goals/goal6'))
        sdgs.append(UNGoals(id=7, title='Affordable and Clean Energy', description='Ensure access to affordable, reliable, sustainable and modern energy for all', link='https://sdgs.un.org/goals/goal7'))
        sdgs.append(UNGoals(id=8, title='Decent Work and Economic Growth', description='Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all', link='https://sdgs.un.org/goals/goal8'))
        sdgs.append(UNGoals(id=9, title='Industry, Innovation and Infrastructure', description='Build resilient infrastructure, promote inclusive and sustainable industrialization and foster innovation', link='https://sdgs.un.org/goals/goal9'))
        sdgs.append(UNGoals(id=10, title='Reduced Inequalities', description='Reduce inequality within and among countries', link='https://sdgs.un.org/goals/goal10'))
        sdgs.append(UNGoals(id=11, title='Sustainable Cities and Communities', description='Make cities and human settlements inclusive, safe, resilient and sustainable', link='https://sdgs.un.org/goals/goal11'))
        sdgs.append(UNGoals(id=12, title='Responsible Consumption and Production', description='Ensure sustainable consumption and production patterns', link='https://sdgs.un.org/goals/goal12'))
        sdgs.append(UNGoals(id=13, title='Climate Action', description='Take urgent action to combat climate change and its impacts', link='https://sdgs.un.org/goals/goal13'))
        sdgs.append(UNGoals(id=14, title='Life Below Water', description='Conserve and sustainably use the oceans, seas and marine resources for sustainable development', link='https://sdgs.un.org/goals/goal14'))
        sdgs.append(UNGoals(id=15, title='Life on Land', description='Protect, restore and promote sustainable use of terrestrial ecosystems, sustainably manage forests, combat desertification, and halt and reverse land degradation and halt biodiversity loss', link='https://sdgs.un.org/goals/goal15'))
        sdgs.append(UNGoals(id=16, title='Peace, Justice and Strong Institutions', description='Promote peaceful and inclusive societies for sustainable development, provide access to justice for all and build effective, accountable and inclusive institutions at all levels', link='https://sdgs.un.org/goals/goal16'))
        sdgs.append(UNGoals(id=17, title='Partnerships for the Goals', description='Strengthen the means of implementation and revitalize the Global partnership for Sustainable Development', link='https://sdgs.un.org/goals/goal17'))
        UNGoals.objects.bulk_create(sdgs)