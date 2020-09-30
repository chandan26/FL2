using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using UMWebApplication.Models;

namespace UMWebApplication.Controllers
{
    public class attendeeController : Controller
    {
        // GET: attendee
        public ActionResult Index()
        {
            using (UMWEBDBEntities1 db = new UMWEBDBEntities1())
            {
                return View(db.attendeeregistrations.ToList());
            }
        }

        // GET: attendee/Details/5
        public ActionResult Details(int? id)
        {
            using (UMWEBDBEntities1 db = new UMWEBDBEntities1())
            {
                return View(db.attendeeregistrations.Where(x => x.registrationid == id).FirstOrDefault());
            }
        }

        // GET: attendee/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: attendee/Create
        [HttpPost]
        public ActionResult Create(attendeeregistration collection)
        {
            try
            {
                using (UMWEBDBEntities1 ab = new UMWEBDBEntities1())
                {
                    ab.attendeeregistrations.Add(collection);
                    ab.SaveChanges();

                }

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }

        // GET: attendee/Edit/5
        public ActionResult Edit(int? id)
        {
            using (UMWEBDBEntities1 db = new UMWEBDBEntities1())
            {
                return View(db.attendeeregistrations.Where(x => x.registrationid == id).FirstOrDefault());
            }
        }

        // POST: attendee/Edit/5
        [HttpPost]
        public ActionResult Edit(int? id, attendeeregistration collection)
        {
            try
            {
                using (UMWEBDBEntities1 a = new UMWEBDBEntities1())
                {
                    a.Entry(collection).State = EntityState.Modified;
                    a.SaveChanges();
                }

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }

        // GET: attendee/Delete/5
        public ActionResult Delete(int? id)
        {
            using (UMWEBDBEntities1 b = new UMWEBDBEntities1())
            {
                return View(b.attendeeregistrations.Where(x => x.registrationid == id).FirstOrDefault());
            }
        }

        // POST: attendee/Delete/5
        [HttpPost]
        public ActionResult Delete(int? id, FormCollection collection)
        {
            try
            {
                using (UMWEBDBEntities1 ab = new UMWEBDBEntities1())
                {
                    attendeeregistration s = ab.attendeeregistrations.Where(x => x.registrationid == id).FirstOrDefault();
                    ab.attendeeregistrations.Remove(s);
                    ab.SaveChanges();
                }

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }
    }
}
