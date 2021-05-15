    def plot(delay_vector):
        plt.style.use('ggplot')
        plt.hist(delay_vector, bins = 10)

        plt.xlabel('Percentage overdue, where 1 is on time (bins = 10)', fontsize=10)
        plt.ylabel('# of projects', fontsize=10)
        plt.title('Duration of construction projects')
        plt.savefig('histogram.jpg')
        plt.show()

        delay_vector.append(df['Week'].iloc[-1])