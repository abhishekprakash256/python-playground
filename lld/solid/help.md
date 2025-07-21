
### 🔠 **SOLID Principles Comparison Table**

| Principle | Full Name                           | Purpose / Goal                                                                   | Similar To             | Differs From                               | Example Scenario                                                                         |
| --------- | ----------------------------------- | -------------------------------------------------------------------------------- | ---------------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **S**     | **Single Responsibility Principle** | A class should have **one and only one reason to change**.                       | Separation of Concerns | Other principles that allow multiple roles | A `User` class handles only user data, not logging or validation.                        |
| **O**     | **Open/Closed Principle**           | Software entities should be **open for extension, but closed for modification**. | Interface Segregation  | LSP, which focuses on substitution         | A `Shape` class lets you add new shapes via subclasses without modifying the base.       |
| **L**     | **Liskov Substitution Principle**   | Subtypes must be **replaceable** for their base types without breaking logic.    | Open/Closed            | SRP — which doesn't care about behavior    | A `Square` class should behave like a `Rectangle` wherever used.                         |
| **I**     | **Interface Segregation Principle** | Clients should not be forced to depend on **interfaces they don't use**.         | Single Responsibility  | LSP — which focuses on replacing subtypes  | A `Printer` interface should be split into `Print` and `Scan` interfaces.                |
| **D**     | **Dependency Inversion Principle**  | High-level modules should not depend on low-level ones. Use **abstractions**.    | Open/Closed            | SRP — focuses on roles, not dependencies   | A `NotificationService` depends on an `INotification` interface, not Email/SMS directly. |

---

### **Similarities Summary**

| Principles         | Similarity                                                               |
| ------------------ | ------------------------------------------------------------------------ |
| **SRP & ISP**      | Both aim to make classes/interfaces focused and minimal.                 |
| **OCP & DIP**      | Both encourage abstraction and decoupling from implementation details.   |
| **LSP & OCP**      | LSP supports OCP by ensuring new subtypes don't break existing behavior. |
| **All Principles** | Improve maintainability, testability, and scalability of OOP systems.    |

---

### **Differences Summary**

| Principle | Key Difference                                                            |
| --------- | ------------------------------------------------------------------------- |
| **SRP**   | Focuses on the **reason to change** a class.                              |
| **OCP**   | Focuses on **extending** behavior without modifying existing code.        |
| **LSP**   | Focuses on **behavioral compatibility** between base and derived classes. |
| **ISP**   | Focuses on **splitting interfaces** to avoid fat contracts.               |
| **DIP**   | Focuses on **reversing dependencies** and depending on abstractions.      |


