PYTHON-Pytest-Decorators

Bir decorator fonksiyonu alır, bazı fonksiyonellikler ekler ve onu döndürür.Fonksiyonun davranışı değiştirmeye yararlar. Fonksiyon çalışmadan önce yapılması 
gereken bir şey varsa veya fonksiyonları dinamik olarak bir yerlere kayıt etmek istiyorsanız decoratorler bu iş için biçilmiş kaftandır.


@pytest.mark.parametrize: Belirli bir test fonksiyonunu farklı parametrelerle çalıştırmak için kullanılır. Bu dekoratörü kullanarak, 
bir testi farklı parametrelerle tekrarlamak yerine, tek bir test fonksiyonunda farklı parametrelerle çalıştırabilirsiniz.
------------------
@pytest.fixture: Uygulamalarımızın durumlarını ve bağımlılıklarını yönetmek için kullanılabilen işlevlerdir.
Test fonksiyonlarından önce veya sonra otomatik olarak çalıştırılır ve testlerde kullanılacak verileri sağlar.
------------------
@pytest.mark.skip: Test işlevlerinin yürütülmesini atlamak için kullanılır.
------------------
@pytest.mark.xfail: Bir testin herhangi bir nedenle başarısız olmasını beklediğiniz anlamına gelir. 
Test başarısız olduğunda, test sonucu "beklenen" bir başarısızlık olarak işaretlenir.
------------------
@pytest.mark.order: Testlerin sırasını belirlemek için kullanılır.
------------------
@pytest.mark.timeout: Testin belirli bir sürede tamamlanması gerektiğini işaret eder.Testin istenen zaman aşımı sınırına ulaşması durumunda testin başarısız olması sağlanır.
------------------
@pytest.mark.slow: Testin yavaş çalıştığını ve diğer testlerin zamanlamasını etkileyebileceğini belirtir.
Bu dekoratör kullanılarak yavaş testlerin belirtilmesi, çalışma zamanı açısından optimize edilebilir.
------------------
@pytest.mark.usefixtures: Belirli bir test için kullanılacak bir veya daha fazla fixture'ı belirtmek için kullanılır. 
Testlerin daha net ve düzenli bir şekilde yazılmasını sağlar.
-----------------
@pytest.mark.dependency:testler arasındaki bağımlılıkları yönetmek için kullanılır.
Bu dekoratörü kullanarak, bir testin yalnızca belirli bir sırayla çalışmasını sağlayabilirsiniz. 
Bu dekoratör icin pytest-dependency" eklentisi yüklü olmasi gereklidir.
----------------
@pytest.mark.filterwarnings: Belirli hata mesajları veya uyarıları filtrelemek veya önemli hale getirmek için kullanılır.
----------------
@pytest.mark.flaky: Testlerin belirli koşullar altında zaman zaman başarısız olabileceği durumlarda kullanılır. 
Bu dekoratörü kullanarak, belirli bir test için belirli bir hata oranı tanımlayabilir ve testin bu oranın üzerinde başarısız olması durumunda tekrarlanmasını sağlayabilirsiniz.
----------------
@pytest.mark.run(order): Testlerin belirli bir sırayla çalışmasını sağlamak için kullanılır. Bu dekoratörü kullanarak, belirli bir testin belirli bir sırada çalışmasını sağlayabilirsiniz.
